from datetime import datetime
import datetime as _dt
import hashlib as _hash
import json as _js
from pickle import TRUE
from random import randint
from tokenize import String
from proof_of_stake import ProofOfStake
from lot import Lot
import string
import random

class Blockchain:
    def __init__(self) -> None:
        self.chain=list()
        initial_block = self.register_user(
            sellers_name="genesis block",property_id=0,previous_hash="0", index=1
        )
        self.chain.append(initial_block)
        
    def compute_nonce(self,sellers_name: str,property_id: int,index: int)->bytes:
        hash_input=str(property_id**2-index**2)+sellers_name
        return hash_input.encode()

    def mine_a_block(self,sellers_name: str,property_id: int) ->dict: 
        previous_block=self.get_previous_block()
        index=len(self.chain)+1
        previous_hash=previous_block["merkel_root"]
        per=test()
        per.print_Validator()
        block=self.register_user(sellers_name=sellers_name,property_id=property_id,previous_hash=previous_hash,index=index)
        return block
        
    def mine_a_transaction(self,sellers_name: str,buyers_name: str,property_id: int) ->dict:
        previous_block=self.get_previous_block()
        index=len(self.chain)+1
        str=buyers_name+sellers_name
        previous_hash=previous_block["merkel_root"]
        block=self.register_transaction(sellers_name,buyers_name,property_id,previous_hash,index)
        return block
        
    def hash_function(self,block)->str:
        encoded_block=_js.dumps(block,sort_keys=True).encode()
        return _hash.sha256(encoded_block).hexdigest()

    def get_previous_block(self) ->dict:
        return self.chain[-1]

    def register_user(self,sellers_name: str,property_id: int,previous_hash: str,index: int) ->dict:
        block={"index":index,
                "sellers_name":sellers_name,
                "buyers_name":None,
                "property_id":property_id,
                "time_stamp":str(_dt.datetime.now()),
                "previous_hash": previous_hash,
                "index": index,
        }
        hash_input=self.compute_nonce(sellers_name,property_id,index)
        block["merkel_root"]=_hash.sha256(hash_input).hexdigest()
        self.chain.append(block)
        return block
    
    def register_transaction(self,sellers_name: str,buyers_name: str,property_id: int,previous_hash: str,index: int) ->dict:
        block={"index":index,
                "sellers_name":sellers_name,
                "buyers_name":buyers_name,
                "property_id":property_id,
                "time_stamp":str(_dt.datetime.now()),
                "previous_hash": previous_hash,
                "index": index
        }
        if(self.verify_buyer_seller(sellers_name,buyers_name,property_id)==0):
            print('Invalid Transaction')
            return 
        st=sellers_name+buyers_name
        hash_input=self.compute_nonce(st,property_id,index)
        block["merkel_root"]=_hash.sha256(hash_input).hexdigest()
        self.chain.append(block)
        return block
    ''' 
        verify buyer seller function checks whether the buyer and seller are registered first 
        and then checks whether the property belongs to seller 
    '''
    def verify_buyer_seller(self,seller: str,buyer: str,property_id: int)->bool :
        i=0
        f=0
        f1=0
        while(i<len(self.chain)):
            cur_block=self.chain[i]
            if(cur_block["buyers_name"]==buyer or cur_block["sellers_name"]==buyer):
                f=1
            if(cur_block["sellers_name"]==seller or cur_block["buyers_name"]==seller):
                f1=1
            i=i+1
        if f1 and f==0:
            return False
        i=len(self.chain)-1
        while i>=0:
            cur_block=self.chain[i]
            if(cur_block["property_id"]==property_id):
                
                if(cur_block["buyers_name"]!=None):
                    if cur_block["buyers_name"]==seller:
                        return True
                    else:
                        return False
                else:
                    if cur_block["sellers_name"]==seller:
                        return True
                    else:
                        return False
            i=i-1
        return False
        
    ''' view_transaction_history function helps to check the total transaction history of the property'''
    def view_transaction_history(self,input_id: int)-> None :
        i=0
        flag=0
        while(i<len(self.chain)):
            b=self.chain[i]
            if(b["property_id"]==input_id):
                if(b["buyers_name"]!=None):
                    print(b["sellers_name"],'sold the property to',b["buyers_name"],"on",b["time_stamp"])
                    flag=1
                else:
                    print('The property Belongs To',b["sellers_name"],b["time_stamp"])
                    flag=1
            i=i+1
        if(flag==0):
            print('Transaction history is not recorded for this property')
class test:            
    def get_random_str(length):
        letters = string.ascii_lowercase
        random_string = "".join(random.choice(letters) for i in range(length))
        return random_string       
    def print_Validator(self)->None :
        pos = ProofOfStake()
        pos.update("Gowtham", 30)
        pos.update("Harsha", 39)
        pos.update("Guru",41)
        
        Gowtham_wins = 0
        Harsha_wins = 0
        Guru_wins=0

        for i in range(100):
            forger = pos.forger(test.get_random_str(i))
            if forger == "Gowtham":
                Gowtham_wins += 1
            elif forger == "Harsha":
                Harsha_wins += 1
            else:
                Guru_wins +=1
        '''print("Gowtham won: " + str(Gowtham_wins) + " times")
        print("Harsha won: " + str(Harsha_wins) + " times")
        print("Guru won: " + str(Guru_wins) + " times")'''
        if(Gowtham_wins>=Harsha_wins and Gowtham_wins>=Guru_wins):
            print("Gowtham is Validating")
        elif(Harsha_wins>=Gowtham_wins and Harsha_wins>=Guru_wins):
            print("Harsha is Validating")
        elif(Guru_wins>=Harsha_wins and Guru_wins>=Gowtham_wins):
            print("Guru is Validating")