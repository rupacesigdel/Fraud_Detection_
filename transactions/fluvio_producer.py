import fluvio
import json

producer = fluvio.topic_producer('transactions')

def produce_transaction(transaction_data):
    producer.send(json.dumps(transaction_data))
