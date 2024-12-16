# findingAccountsByTags_inAWS

Another script created at work, in order to save time.

I created this script to make my life easier when it comes to finding out who is the account owners and contacts of certain accounts in our organization. 
For example, at line 38 and 39, I would update the code with a tag name like "mandate code" and the value being the account im investigating, and than it filter through the organization with accounts that match those tags.

AWS Organizations allows tagging accounts with key-value pairs, and you can use the list_tags_for_resource API to retrieve tags for each account.
list_accounts: Retrieves all accounts in your AWS organization.
list_tags_for_resource: Retrieves the tags for a specific account using its ID.
Filtering by tag: Compares the key and value of each tag to find matches.
