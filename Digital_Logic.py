import tkinter as tk

Items = []
Cables = []
PowerSources = []
Zeroes = []
Gates = []
Outputs = []
lines = 0
points = 1
multiplier = 30


class Win:

    def __init__(self, root):
        Board = tk.Canvas(root, width=1200, height=800, bg="white")
        Board.pack()
        Buttons = tk.Frame(root, width=1200, height=100)
        Buttons.pack(side="left")
        self.Board = Board
        self.create_board(Board)
        self.create_buttons(Buttons)
        self.item = ""
        self.cords1 = [-1, -1]
        self.cords2 = [-1, -1]

    def create_board(self, Board):
        if lines == 1:
            for x in range(multiplier, 1200, multiplier):
                Board.create_line(x, 1, x, 800)

            for y in range(multiplier, 800, multiplier):
                Board.create_line(1, y, 1200, y)
        if points == 1:
            for x in range(multiplier, 1200, multiplier):
                for y in range(multiplier, 800, multiplier):
                    Board.create_oval(x - 1, y - 1, x + 1, y + 1)

    def create_buttons(self, Buttons):
        button_color = "light blue"
        button_powersource = tk.Button(Buttons, width=8, height=6, bg=button_color, text="PS",
                                       command=self.b_powersource)
        button_powersource.pack(side="left")
        button_zero = tk.Button(Buttons, width=8, height=6, bg=button_color, text="ZERO", command=self.b_zero)
        button_zero.pack(side="left")
        button_not = tk.Button(Buttons, width=8, height=6, bg=button_color, text="NOT", command=self.b_not)
        button_not.pack(side="left")
        button_and = tk.Button(Buttons, width=8, height=6, bg=button_color, text="AND", command=self.b_and)
        button_and.pack(side="left")
        button_or = tk.Button(Buttons, width=8, height=6, bg=button_color, text="OR", command=self.b_or)
        button_or.pack(side="left")
        button_cable = tk.Button(Buttons, width=8, height=6, bg=button_color, text="CABLE", command=self.b_cable)
        button_cable.pack(side="left")
        button_output = tk.Button(Buttons, width=8, height=6, bg=button_color, text="OUTPUT", command=self.b_output)
        button_output.pack(side="left")

        button_start_simulation = tk.Button(Buttons, width=8, height=6, bg="green", text="RUN",
                                            command=self.start_simulation)
        button_start_simulation.pack(side="right")

    def start_simulation(self):

        # for i in Items:
        #     i.active = 0
        # for i in Gates:
        #     i.power = 0
        # try:
        #     for i in range(0, len(Cables)):
        #         Cables.remove(Cables[i])
        #         Items.remove(Cables[i])
        # except:
        #     pass
        for i in Cables:
            i.power = 0

        for i in Outputs:
            i.power = 0

        for i in PowerSources:
            i.power_up()

        for i in Zeroes:
            i.send_zero()
        go = 0
        while go == 0:
            go = 1

            for i in Gates:
                if i.active == 0:
                    go = 0
                    try:
                        i.activate()
                    except:
                        pass
        for i in Outputs:
            i.activate()

    def b_output(self):
        self.Board.bind("<Button-1>", self.get_mouse_cords)
        self.item = "output"

    def b_powersource(self):
        self.Board.bind("<Button-1>", self.get_mouse_cords)
        self.item = "powersource"

    def b_zero(self):
        self.Board.bind("<Button-1>", self.get_mouse_cords)
        self.item = "zero"

    def b_not(self):
        self.Board.bind("<Button-1>", self.get_mouse_cords)
        self.item = "not"

    def b_and(self):
        self.Board.bind("<Button-1>", self.get_mouse_cords)
        self.item = "and"

    def b_or(self):
        self.Board.bind("<Button-1>", self.get_mouse_cords)
        self.item = "or"

    def b_cable(self):
        self.Board.bind("<Button-1>", self.get_mouse_cords)
        self.item = "cable"

    def get_mouse_cords(self, event):
        self.Board.unbind("<Button-1>")
        if self.item == "cable":
            if self.cords1 == [-1, - 1]:
                self.cords1 = [((abs(event.x - multiplier / 2)) // multiplier) + 1,
                               ((abs(event.y - multiplier / 2)) // multiplier) + 1]
                self.b_cable()
            elif self.cords2 == [-1, -1]:
                self.cords2 = [((abs(event.x - multiplier / 2)) // multiplier) + 1,
                               ((abs(event.y - multiplier / 2)) // multiplier) + 1]
                self.create_cable((self.cords1[0] * multiplier, self.cords1[1] * multiplier),
                                  (self.cords2[0] * multiplier, self.cords2[1] * multiplier))
                self.cords1 = [-1, -1]
                self.cords2 = [-1, -1]
        else:
            self.cords1 = [((abs(event.x - multiplier / 2)) // multiplier) + 1,
                           ((abs(event.y - multiplier / 2)) // multiplier) + 1]
            if self.item == "and":
                self.create_and(self.cords1[0] * multiplier, self.cords1[1] * multiplier)
            if self.item == "or":
                self.create_or(self.cords1[0] * multiplier, self.cords1[1] * multiplier)
            if self.item == "not":
                self.create_not(self.cords1[0] * multiplier, self.cords1[1] * multiplier)
            if self.item == "powersource":
                self.create_powersource(self.cords1[0] * multiplier, self.cords1[1] * multiplier)
            if self.item == "zero":
                self.create_zero(self.cords1[0] * multiplier, self.cords1[1] * multiplier)
            if self.item == "output":
                self.create_output(self.cords1[0] * multiplier, self.cords1[1] * multiplier)
            self.cords1 = [-1, -1]
            self.cords2 = [-1, -1]

    def create_cable(self, cords1, cords2):
        cable = Cable(cords1[0], cords1[1], cords2[0], cords2[1])
        Items.append(cable)
        Cables.append(cable)
        self.Board.create_line(cords1[0], cords1[1], cords2[0], cords2[1], width=5, fill="red")

    def create_and(self, x, y):
        And = Gate(x, y, "AND")
        Items.append(And)
        Gates.append(And)
        self.draw_and(x, y)

    def draw_and(self, x, y):
        self.Board.create_arc(x - multiplier, y - multiplier, x + multiplier, y + multiplier, start=270, extent=180,
                              fill="blue")

    def create_or(self, x, y):
        Or = Gate(x, y, "OR")
        Items.append(Or)
        Gates.append(Or)
        self.draw_or(x, y)

    def draw_or(self, x, y):
        points1 = [x, y, x - multiplier / 6, y - multiplier / 2, x - multiplier / 2, y - multiplier]
        points2 = [x, y - 3 * multiplier / 4, x + multiplier / 2, y - multiplier * 2 / 5, x + multiplier, y]
        points3 = [x + multiplier / 2, y + multiplier * 2 / 5, x, y + 3 * multiplier / 4]
        points4 = [x - multiplier / 2, y + multiplier, x - multiplier / 6, y + multiplier / 2]
        points = points1 + points2 + points3 + points4
        self.Board.create_polygon(points, fill="orange")

    def create_not(self, x, y):
        Not = Gate(x, y, "NOT")
        Items.append(Not)
        Gates.append(Not)
        self.draw_not(x, y)

    def draw_not(self, x, y):
        points = [x, y - multiplier / 2, x + multiplier * 2 / 3, y, x, y + multiplier / 2]
        self.Board.create_polygon(points, fill="grey", outline="black")
        x1 = x + 5 * multiplier / 6
        y1 = y
        self.Board.create_oval(x1 - multiplier / 6, y1 - multiplier / 6, x1 + multiplier / 6, y1 + multiplier / 6,
                               fill="grey")

    def create_zero(self, x, y):
        zero = Zero(x, y)
        Items.append(zero)
        Zeroes.append(zero)
        self.draw_zero(x, y)

    def draw_zero(self, x, y):
        self.Board.create_rectangle(x - multiplier / 2, y - multiplier / 2, x + multiplier / 2, y + multiplier / 2,
                                    fill="white")

    def create_powersource(self, x, y):
        Powersource = PowerSource(x, y)
        Items.append(Powersource)
        PowerSources.append(Powersource)
        self.draw_powersource(x, y)

    def draw_powersource(self, x, y):
        self.Board.create_rectangle(x - multiplier / 2, y - multiplier / 2, x + multiplier / 2, y + multiplier / 2,
                                    fill="yellow")

    def create_output(self, x, y):
        output = Output(x, y, self.Board)
        Items.append(output)
        Outputs.append(output)
        self.draw_output(x, y)

    def draw_output(self, x, y):
        self.Board.create_oval(x - multiplier / 2, y - multiplier / 2, x + multiplier / 2, y + multiplier / 2,
                               fill="grey")


class Cable:

    def __init__(self, startx, starty, endx, endy):
        self.startx = startx
        self.starty = starty
        self.endx = endx
        self.endy = endy
        self.power = 0
        self.active = 0

    def power_on(self):
        self.active = 1
        self.power = 1

    def power_off(self):
        self.active = 1
        self.power = 0


class PowerSource:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.active = 0

    def power_up(self):
        self.active = 1
        for cable in Cables:
            if cable.startx == self.x and cable.starty == self.y:
                cable.power_on()


class Zero:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.active = 0

    def send_zero(self):
        self.active = 1
        for cable in Cables:
            if cable.startx == self.x and cable.starty == self.y:
                cable.power_off()


class Gate:

    def __init__(self, startx, starty, type):
        self.startx = startx
        self.starty = starty
        self.endx = startx + multiplier
        self.endy = starty
        self.active = 0
        self.power = 0
        self.type = type

    def activate(self):
        Inputs = []
        if self.active == 0:

            for cable in Cables:
                if cable.endx == self.startx and cable.endy == self.starty:
                    if cable.active == 0:
                        return

            for cable in Cables:

                if cable.endx == self.startx and cable.endy == self.starty:
                    if cable.power == 1:
                        Inputs.append(1)
                    else:
                        Inputs.append(0)
            print(self.type, Inputs)
            self.check_inputs(Inputs)
        else:
            return

    def check_inputs(self, Inputs):
        self.active = 1

        if self.type == "AND":
            self.power = 1
            for x in Inputs:
                if x == 0:
                    self.power = 0
                    break

        if self.type == "OR":
            self.power = 0
            for x in Inputs:
                if x == 1:
                    self.power = 1
                    break
        if len(Inputs) == 0:
            self.power = 0

        if self.type == "NOT":
            self.power = 1 - Inputs[0]

        self.send_signal()

    def send_signal(self):
        for cable in Cables:
            if cable.startx == self.endx and cable.starty == self.endy:
                if self.power == 1:
                    cable.power_on()
                else:
                    cable.power_off()


class Gate:

    def __init__(self, startx, starty, type):
        self.startx = startx
        self.starty = starty
        self.endx = startx + multiplier
        self.endy = starty
        self.active = 0
        self.power = 0
        self.type = type

    def activate(self):
        Inputs = []
        if self.active == 0:
            for cable in Cables:
                if cable.endx == self.startx and cable.endy == self.starty:
                    if cable.active == 0:
                        return
            for cable in Cables:

                if cable.endx == self.startx and cable.endy == self.starty:
                    if cable.power == 1:
                        Inputs.append(1)
                    else:
                        Inputs.append(0)
            print(self.type, Inputs)
            self.check_inputs(Inputs)
        else:
            return

    def check_inputs(self, Inputs):
        self.active = 1

        if self.type == "AND":
            self.power = 1
            for x in Inputs:
                if x == 0:
                    self.power = 0
                    break

        if self.type == "OR":
            self.power = 0
            for x in Inputs:
                if x == 1:
                    self.power = 1
                    break
        if len(Inputs) == 0:
            self.power = 0

        if self.type == "NOT":
            self.power = 1 - Inputs[0]

        self.send_signal()

    def send_signal(self):
        for cable in Cables:
            if cable.startx == self.endx and cable.starty == self.endy:
                if self.power == 1:
                    cable.power_on()

                else:
                    cable.power_off()


class Output:

    def __init__(self, x, y, Board):
        self.Board = Board
        self.x = x
        self.y = y
        self.power = 0
        self.active = 0

    def activate(self):
        Input = 0
        if self.active == 0:
            for cable in Cables:
                if cable.endx == self.x and cable.endy == self.y:
                    if cable.active == 0:
                        break

            for cable in Cables:
                if cable.endx == self.x and cable.endy == self.y:
                    if cable.power == 1:
                        Input = 1
                    break
            self.result(Input)
        else:
            return

    def result(self, inp):

        if inp == 1:
            self.Board.create_oval(self.x - multiplier / 2, self.y - multiplier / 2, self.x + multiplier / 2,
                                   self.y + multiplier / 2, fill="yellow")
        if inp == 0:
            self.Board.create_oval(self.x - multiplier / 2, self.y - multiplier / 2, self.x + multiplier / 2,
                                   self.y + multiplier / 2, fill="white")


root = tk.Tk()
root.geometry("1200x900+10+10")
root.configure(bg="#96DFCE")
Win(root)

root.mainloop()
