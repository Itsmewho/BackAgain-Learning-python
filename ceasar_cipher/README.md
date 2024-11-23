Make a ceasar cipher!

Encrypt and decript messages.
Store messages on MONGOBD.

- Only registered users can use caesar
- Resgistered users need to accept invite to get secure message (only shared between user a and b / a and c,.. b and c will get another one)
- Check if user already exsist.
- Delete user if requested
- If Delete user -> delete all data that correspond with user ID (Even if its a party! Gone is Gone )
- Invite consist of user name, surname, phonenumber, message for invitated user and accept or decline option
- Invited need to exist else: ERROR-message:
- Handle edge cases like invalid user IDs, non-existent invites, or missing secure IDs.
- Message can be encrypted and decryped by secure party ID -> created when invite is accepted.
- Use a secure random generator to create IDs (e.g., uuid.uuid4() or SHA-256).

- Invitated party gets contacts list (expand for a and b but if theres a -> c, b can not see c)
- A message can only be sent between party's
- Sent message are sent and received from database

Input() options:

invite from a - show / delete
if shown read invite accept / decline
show contact list:
sent invite to...
sent message to....
show messages from,....
delete messages? (delete all message data also from receiving party's)
delete account... - Are you sure? (y/n)

if message received give message: onread message wanna read it? :

- person sent
- message
- option send answer? (y/n)

Quit program at any time.

#

#

Learing points: ------------------>

#

Working with databases.

CRUD operations.

File-system.

Logic.

Function naming and params

Good comments

Dont forget a .env .gitignore and pip install pipreqs ---> pipreqs /path/to/project

Try to keep the collections 'hidden' use .env - > MONGO_DBENCRIPT, MONGO_DECRIPT or something like that:

MONGO_URI=connect

MONGO_DBNAME=secure_messaging

MONGO_DBCONTACT=users
MONGO_DBCONTACTLIST=contact_list
MONGO_DBINVITES=invitations
MONGO_DBMESSAGES=messages
