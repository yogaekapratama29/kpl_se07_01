class VendingMachineFSM:
    def __init_fsm__(self):
        self.state = "Idle"
        
        
        self.transitions = {
            "Idle": {"insert_coin": "Waiting for Product"},
            "Waiting for Product": {"select_product": "Releasing Product", "cancel": "Idle"},
            "Releasing Product": {"dispense": "Finished"},
            "Finished": {"reset": "Idle"}
        }
    
    def trigger(self, action):
        if action in self.transitions[self.state]:
            self.state = self.transitions[self.state][action]
            print(f"State changed to: {self.state}")
        else:
            print(f"Invalid action '{action}' in state '{self.state}'")


fsm = VendingMachineFSM()
fsm.__init_fsm__()
fsm.trigger("insert_coin")   
fsm.trigger("select_product") 
fsm.trigger("dispense")      
fsm.trigger("reset")         