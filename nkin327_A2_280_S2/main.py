import mysql.connector
from drones import Drone, DroneStore

class Application(object):
    """ Main application wrapper for processing input. """

    def __init__(self, conn):
        self._drones = DroneStore(conn)
        self._commands = {
            'list': self.list,
            'add': self.add,
            'update': self.update,
            'remove': self.remove,
            'allocate': self.allocate,
            'help': self.help,
        }

    def main_loop(self):
        print('Welcome to DALSys')
        cont = True
        while cont:
            val = input('> ').strip().lower()
            cmd = None
            args = {}
            if len(val) == 0:
                continue

            try:
                parts = val.split(' ')
                if parts[0] == 'quit':
                    cont = False
                    print('Exiting DALSys')
                else:
                    cmd = self._commands[parts[0]]
            except KeyError:
                print('!! Unknown command "%s" !!' % (val))

            if cmd is not None:
                args = parts[1:]
                try:
                    cmd(args)
                except Exception as ex:
                    print('!! %s !!' % (str(ex)))

    def add(self, args):
        rescuetag = False
        addy = conn.cursor()
        addquery = "INSERT INTO drones(Name, Class_Type, Rescue) VALUES ("
        if("-class" in args[0]):
            raise Exception("name is required");
        elif(args[0] == "-rescue"):
            raise Exception("name is required");
        for i in range(len(args)):
            if ("-rescue" in args[i]):
                rescuetag = True
                break; 
            if ("-class=" in args[i]):
                addquery += ", {0}".format(args[i].lstrip("-class="))
            else:
                addquery += "{0}".format(args[i]);
        if (rescuetag):
            addquery += ", 1)" 
        else:
            addquery += ", 0)"
        print(addquery)
        addy.execute(addquery)
        conn.commit()
            

    def allocate(self, args):
        if len(args) == 0:
            raise Exception("ID is required")
        if (not args[0].isdigit()):
            raise Exception("ID is required")

    def help(self, args):
        """ Displays help information. """
        print("Valid commands are:")
        print("* list [- class =(1|2)] [- rescue ]")
        print("* add 'name ' -class =(1|2) [- rescue ]")
        print("* update id [- name ='name '] [- class =(1|2)] [- rescue ]")
        print("* remove id")
        print("* allocate id 'operator'")

    def list(self, args):
        self._drones.list_all(args);
            
            

    def remove(self, args):
        removequery = "DELETE FROM drones"
        mycursor = conn.cursor()
        rem = conn.cursor()
        if len(args) == 0:
            raise Exception("ID is required")
        if (not args[0].isdigit()):
            raise Exception("ID is required")
        mycursor.execute("SELECT * FROM drones WHERE ID = {}".format(args[0]))
        mycursor.fetchone()
        if (mycursor.rowcount == 0):
            raise Exception("Unknown drone")
        else:
            removequery += " WHERE ID = {0}".format(args[0])
            rem.execute(removequery)
            conn.commit()
            print("Drone removed")

    def update(self, args):
        rescuetag = False
        list0 = []
        mycursor = conn.cursor()
        string = "UPDATE drones SET"
        if len(args) == 0:
            raise Exception("ID is required")
        if (not args[0].isdigit()):
            raise Exception("ID is required")
        mycursor.execute("SELECT * FROM drones WHERE ID = {0}".format(args[0]))
        row = mycursor.fetchone()
        if (mycursor.rowcount == 0):
            raise Exception("Unknown drone")    
        for x in args:  
                if ("-name" in x) :
                    i = args.index(x)
                    string += " Name = {0}".format(args[i].lstrip("-name="))
                elif ("-class" in x):
                    i = args.index(x)
                    string += ", Class_Type = {0}".format(args[i].lstrip("-class="))
                elif ("-rescue" in x):
                    rescuetag = True
        if (rescuetag):
            string += ", Rescue = 1" 
        else:
            string += ", Rescue = 0"
        print("Updated drone with ID 000{0}:\n -set name to {1}".format(args[0], args[1].lstrip("-name='").rstrip("'")))
        string += " WHERE ID = {0}".format(args[0])   
        mycursor.execute(string)
        conn.commit()
                

if __name__ == '__main__':
    conn = mysql.connector.connect(user='root',
                                   password='admin',
                                   host='127.0.0.1',
                                   database='test')
    app = Application(conn)
    app.main_loop()
    conn.close()
