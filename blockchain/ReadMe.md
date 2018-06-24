For the devs:

1. Deploy the 'hello world' contract as mentioned in the tutorial on 
`https://github.com/Nebulas-Learning/Nebulas-Learning/blob/master/Hackathon-Presentation.pdf`

2. After deploying the contract, ie after pressing the 'Submit' button on the 'Deploy' tab, you will get a 'txhash' and a 'contract_address'. Note them down

3. Go to the 'Call' tab. Fill in the function and arguments. In the 'To Address' fill up the 'contract_address' from step 2. Enter the key and password. Click on the 'Test' button and then click 'Submit'.

4. Note down the new 'txhash'

5. Execute this command in the terminal 

`curl -i -H 'Content-Type: application/json' -X POST https://testnet.nebulas.io/v1/user/getEventsByHash -d '{"hash":"the new tx hash you just noted down in step 4"}'`

You will get a result like this

`{"result":{"events":[{"topic":"chain.contract.greetings","data":"\"Here is Mumbai my friend.\""},{"topic":"chain.transactionResult","data":"{\"hash\":\"a2390619c8b730e269acf7d7cc8e530f0252211a44785ba494526db56f9db309\",\"status\":1,\"gas_used\":\"20199\",\"error\":\"\",\"execute_result\":\"\\\"\\\"\"}"}]}}`


Watch out for the data object in the response on the first line. My input was "Here is "+city+"My friend" in the request. My argument was "Mumbai".
