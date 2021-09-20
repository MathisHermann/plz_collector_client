# plz_collector_client
Client that runs a Python script to save postal codes. If there is an active internet connection, the codes can be sent to a remote server.

To enable the remote storage of the data set the variable `safe_on_remote_server = True` and define the endpoint `data_target_url`to the individual value.

This Script uses the Fernet Library to encrypt the data. Therefore, an encryption-key must be provided to encrypt the data locally and decrypt the data remotely.  
To generate a new key run  
```
new_key = Fernet.generate_key()
print(new_key)
```
This will print a key, which then has to be saved (e.g.):  
```
ENCRYPTION_KEY = b'72SllJD3iLOnWk5K_wwp-rqJ4tq7ubG_FEYy7zvIjII='
```
The format has to be exactly as shown in the example. If not, the encryption won't run correctly.