import random

class Coin:

    def __init__(self, rare= False, clean = True, heads = True, **kwargs):
        #for key,value in kwargs.items():

        self.is_rare = rare
        self.is_clean = clean
        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value

    def rust(self):
        self.color = self.rusty_color

    def clean(self):
        self.color = self.clean_color

    def __del__(self):
        print("destructor called")

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

# class Pound(Coin):
#     def __init__(self):
#         dict_data = {
#         "original_value": 1.0,
#         "clean_color": "gold",
#         "rusty_color": "greenish",
#         "num_edges": 1.0,
#         "diameter":22.5, #mm
#         "thickess":3.15 , #mm
#         "mass":9.5 #gm
#         }
#
#     super().__init__(**dict_data)







# class Pound:
#
#     def __init__(self, rare=False):   #constructor
#         self.rare = rare
#         if self.rare:
#             self.value = 1.25
#         else:
#             self.value = 1.0
#         if self.is_clean:
#             self.color = self.clean_color
#         else:
#             self.color = self.rusty_color
#
#
#
#         #self.value = 1.0
#         self.color = "gold"
#         self.num_edges = 1
#         self.diameter = 22.5  # milimeter
#         self.thickness = 3.15  # milimeter
#         self.heads = True  # if false that means tails
#
#     def rust(self):
#         self.color = "greenish"
#
#     def clean(self):
#         self.color = "gold"
#
#     def flip(self):
#         heads_options = [True, False]
#         choice = random.choice(heads_options)
#         self.heads = choice
#
#     def __del__(self):
#         print("Coin Spent...!")
#
#
# coin1 = Pound()
# # #coin2 = Pound()
# #
# # # coin1.color = "greenish"
# # print(coin1.color)
# # #print(coin2.color)
# #
# # coin1.rust()
# # print("rusty",coin1.color)
# #
# # coin1.clean()
# # print("cleaned",coin1.color)
# #
# # coin1 = Pound()
# # print("default side",coin1.heads)
# # coin1.flip()
# # print("flipping",coin1.heads)
#
# del coin1
