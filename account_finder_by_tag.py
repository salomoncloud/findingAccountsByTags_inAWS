import boto3

def get_accounts_with_tag(key, value):
    # Initialize Organizations client
    client = boto3.client('organizations')
    
    # Get all accounts in the organization
    accounts = []
    paginator = client.get_paginator('list_accounts')
    for page in paginator.paginate():
        accounts.extend(page['Accounts'])
    
    # Filter accounts based on the tag
    tagged_accounts = []
    for account in accounts:
        account_id = account['Id']
        try:
            # Retrieve tags for the account
            tags_response = client.list_tags_for_resource(ResourceId=account_id)
            tags = tags_response.get('Tags', [])
            
            # Check if the desired tag exists
            for tag in tags:
                if tag['Key'] == key and tag['Value'] == value:
                    tagged_accounts.append({
                        'AccountId': account_id,
                        'AccountName': account['Name']
                    })
                    break
        except client.exceptions.AccessDeniedException:
            print(f"Access denied for account {account_id}. Ensure your role has permissions.")
        except Exception as e:
            print(f"Error processing account {account_id}: {e}")
    
    return tagged_accounts

if __name__ == "__main__":
    tag_key = "name of the tag"
    tag_value = "value for this tag"
    accounts_with_tag = get_accounts_with_tag(tag_key, tag_value)
    
    if accounts_with_tag:
        print("Accounts with the specified tag:")
        for account in accounts_with_tag:
            print(f"Account ID: {account['AccountId']}, Name: {account['AccountName']}")
    else:
        print("No accounts found with the specified tag.")
