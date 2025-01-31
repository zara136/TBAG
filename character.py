class Character:
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        print(self.name + " is here")
        print(self.description)

    def set_conversation(self, conversation):
        self.conversation = conversation

    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True
    
    def sleep(self):
        print("you cannot hypnotise them")
    
    def gift(self, gift_item):
        print("why would you want to gift " + self.name + "?!")
    
class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness
        
    def get_weakness(self):
        return self.weakness
    
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("you fend " + self.name + " off with the " + combat_item )
            return True
        else:
            print(self.name + " crushes you, puny adventurer")
            return False
        
    def sleep(self):
        print("you hypnotise " + self.name + " and they fall asleep")

class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.favourite = None

    def set_favourite(self, favourite_item):
        self.favourite = favourite_item

    def get_favourite(self):
        return self.favourite
    
    def gift(self, gift_item):
        if gift_item == self.favourite:
            print(self.name + " loves it! " + gift_item + " is their favourite")
            return True
        else:
            print(gift_item + " isn't " + self.name + "'s favourite, but they accept it nonetheless" )

    def hug(self):
        print("you give " + self.name + " a big friendly hug")
    