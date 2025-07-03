from ai import AI
from todolist import Todo, Item
import pyjokes


alf = AI()
todo = Todo()

def make_joke():
    funny = pyjokes.get_joke()
    print(funny)
    alf.say(funny)

def add_todo()->bool:
    item = Item()
    alf.say("Tell me what to add to the list")
    try:
        item.title = alf.listen()
        todo.new_item(item)
        message = "Added " + item.title
        alf.say(message)
        return True
    except:
        print("oops there was an error")
        return False
    
def list_todos():
    if len(todo) > 0:
        alf.say("Here are your to do's")
        for item in todo:
            alf.say(item.title)
    else:
        alf.say("The to do list is empty!")

def remove_todo()->bool:
    alf.say("Tell me which item to remove")
    try:
        item_title = alf.listen()
        todo.remove_item(title=item_title)
        message = "Removed " + item_title
        alf.say(message)
        return True
    except:
        print("opps there was an error")
        return False
    

command = ""
while True and command != "goodbye":
    command = alf.listen()
    print("This was what you told me:", command)

    if command == "tell me a joke" or command == "give me a joke":
        make_joke()
        command = ""
    if command in ["add to-do","add to do", "add item"]:
        add_todo()
        command = ""
    if command in ["list todos", "list todo", "list to do", "list to-do", "list to do's",'list items']:
        list_todos()
        command = ""
    if command in ["remove todo", "remove item", "mark done", "remove todos", "remove to-do", "remove to do's"]:
        remove_todo()
        command = ""

alf.say("Goodbye")

