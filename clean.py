from google.cloud import pubsub_v1

# Set your Google Cloud project ID
project_id = "cloud-kumari-kumari-400603"

# Set your topic name
topic_name = "sample"

# Create a subscriber client
subscriber = pubsub_v1.SubscriberClient()

# Get the fully qualified topic path
topic_path = subscriber.topic_path(project_id, topic_name)

# List all subscriptions
subscriptions = subscriber.list_subscriptions(project=f"projects/{project_id}")

# Iterate over subscriptions and delete messages from the topic
for subscription in subscriptions:
    if topic_path in subscription.topic:
        subscription_path = subscription.name
        subscriber.delete_subscription(request={"subscription": subscription_path})
        print(f"All messages in subscription '{subscription_path}' have been deleted.")

print(f"All messages in topic '{topic_path}' have been deleted.")
