from tkinter import *


class TitlePage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        # self.create_button()
        # self.parent = parent
        btn = Button(
            self,
            text='Zaczynamyyyyyyyyyyyyyyyyyyyyyyy !',
            bd='3',
            command=controller.start_quiz,
            width=10,
            height=3,
        )
        btn.pack(side="top")
        #btn.place(x=700, y=450)

    # def create_button(self):
    #     btn = Button(
    #         self.parent,
    #         text='Zacznij grę !',
    #         bd='3',
    #         command=self.parent.destroy,
    #         width=10,
    #         height=3,
    #     )
    #     # btn.pack(side="top")
    #     btn.place(x=700, y=450)
