from config import current_config


def form_refund_config(application_id, ordering_channel, channel_config, request_application_refund_config):
    brand_config = channel_config.get(application_id, {})
    brand_config.setdefault("PREPAID", {})
    brand_config.setdefault("NON_PREPAID", {})

    partner_pay = request_application_refund_config["partner_pay"]
    is_prepaid_manual_refund = request_application_refund_config["is_prepaid_manual_refund"]
    is_non_prepaid_manual_refund = request_application_refund_config["is_non_prepaid_manual_refund"]
    prepaid_refund_init_states = request_application_refund_config["refund_initiation_states_for_prepaid_orders"]
    non_prepaid_refund_init_states = request_application_refund_config["refund_initiation_states_for_non_prepaid_orders"]

    brand_config["PREPAID"]["PREPAID"] = {
        "AUTO_INITIATE": prepaid_refund_init_states if not is_prepaid_manual_refund else ["refund_approved"],
        "FINANCE": [] if not is_prepaid_manual_refund else prepaid_refund_init_states
    }
    brand_config["PREPAID"]["IS_PARTNER_PAY"] = partner_pay

    brand_config["NON_PREPAID"]["NON_PREPAID"] = {
        "AUTO_INITIATE": non_prepaid_refund_init_states if not is_non_prepaid_manual_refund else ["refund_approved"],
        "FINANCE": [] if not is_non_prepaid_manual_refund else non_prepaid_refund_init_states
    }
    brand_config["NON_PREPAID"]["IS_PARTNER_PAY"] = partner_pay
    
    return brand_config


def insert_refund_config(application_refund_config_to_inserted):
    computron_db = current_config.mongo_computron_write
    COLLECTION_NAME = "refund_static_config"
    conditions = {"conditions.ordering_channel": "all_channels"}

    for request_application_refund_config in application_refund_config_to_inserted:
        ordering_channel = request_application_refund_config["ordering_channel"]
        application_id = request_application_refund_config["application_id"]

        refund_config_obj = computron_db[COLLECTION_NAME].find_one(conditions)
        refund_config = refund_config_obj.get("config", {})
        channel_config = refund_config.get(ordering_channel, {})

        if channel_config:
            brand_config = form_refund_config(
                application_id, ordering_channel, channel_config,
                request_application_refund_config
            )

            refund_config[ordering_channel][application_id] = brand_config
            computron_db[COLLECTION_NAME].update_one(conditions, {"$set": {"config": refund_config}})
            print(
                "Refund configuration updated successfully for app_id: {}, ordering_channel: {}".format(
                    application_id, ordering_channel
                )
            )
        else:
            print(
                "Ordering channel specific configuration not found in the database for app_id: {}, ordering_channel: {}".format(
                    application_id, ordering_channel
                )
            )





# Please provide auto/manual refund configuration
"""
case - 1
manual_refund = True
the states on which refund is triggered, status will be changed
to refund_pending_for_approval and once its approved by finance team, refund will be initiated.

case - 2
manual_refund = False
the states on which refund is triggered, refund will be auto initiated and no approval required from finance team.
"""


# please provice the partner pay configuration
"""
case - 1
partner_pay = True
if the refund needs to be done by brand. In this case Avis will only perform refund_initiated state transition.

case - 2
partner_pay = False
if the refund needs to be done by Fynd. In this case Avis will perform refund_initiated state transition
and it will also initiate the refund request to gringotts to process the refund.

"""

application_refund_config_to_inserted = [
    {
        "application_id": "667120db8c8dc2e010c99af3",
        "ordering_channel": "ECOMM",  # update the ordering_channel for given application_id
        "refund_initiation_states_for_prepaid_orders": [
            "cancelled_customer","cancelled_fynd","bag_lost","return_bag_lost","rto_bag_lost","return_accepted",
            "rto_bag_accepted","return_bag_picked"
          ],
        "refund_initiation_states_for_non_prepaid_orders": [
        ],
        "is_prepaid_manual_refund": False,
        "is_non_prepaid_manual_refund": True,
        "partner_pay": False
    }
]




# calling function to insert/update the refund config for above given applications

insert_refund_config(application_refund_config_to_inserted)