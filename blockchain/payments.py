import subprocess
from subprocess import Popen, PIPE
import re
from string import printable

class payments(object):
	def __init__(self):
		pass

	def params(self):
		"""
		Returns nounce of current account.
		"""
		nounce = subprocess.check_output(["bash", "curl_params.sh"])
		nounce = nounce.split("{")
		for n in nounce:
			if "balance" in n:
				check_balance = n.split(",")
				actual_balance = check_balance[0].split(":")[1]
				nounce = check_balance[1].split(":")[1]
				type_of_txn = check_balance[2].split(":")[1]
				actual_balance = actual_balance.replace('"', '')
				nounce = nounce.replace('"', '')
				type_of_txn = type_of_txn.replace('"', '')
				if "}}" in type_of_txn:
					type_of_txn = type_of_txn.replace("}}", "")
				
				print int(actual_balance), int(nounce), int(type_of_txn)

	def _secure_list(self):
		"""
		List of active users of the smart contract for the hotel room.
		"""




	def check_in(self):
		"""
		Takes the information provided from the hotel and uses it to deploy a smart contract associated with
		the user's wallet. It transfers money after checking balance (two txns: deposit, rental/night). 
		"""
		#c_in = subprocess.check_output(["bash", "curl_contract.sh"])
		


getTransactionReceipt(aaebb86d15ca30b86834efb600f82cbcaf2d7aaffbe4f2c8e70de53cbed17889)

	def check_out(self):
		"""
		Returns the deposit back to the user from another wallet. The ID is removed from the secure list. 
		"""

a = payments()
a.check_in()

