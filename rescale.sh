#!/bin/bash

rm -rf json/images_chatbot
cp -r json/images json/images_chatbot

# convert json/images_chatbot/Avoid_the_River_image_0.png -resize 50% json/images_chatbot/Avoid_the_River_image_0.png # size:    7360
# convert json/images_chatbot/Benford_s_Law_image_0.png -resize 50% json/images_chatbot/Benford_s_Law_image_0.png # size:   15207
convert json/images_chatbot/Benford_s_Law_image_1.png -resize 50% json/images_chatbot/Benford_s_Law_image_1.png # size:   33657
convert json/images_chatbot/Benford_s_Law_image_2.png -resize 50% json/images_chatbot/Benford_s_Law_image_2.png # size:   35367
convert json/images_chatbot/Card_Sums_image_0.png -resize 30% json/images_chatbot/Card_Sums_image_0.png # size:   20935
# convert json/images_chatbot/Colouring_image_0.png -resize 50% json/images_chatbot/Colouring_image_0.png # size:    1484
# convert json/images_chatbot/Colouring_image_1.png -resize 50% json/images_chatbot/Colouring_image_1.png # size:    2022
convert json/images_chatbot/Colouring_image_2.png -resize 20% -background white -alpha remove json/images_chatbot/Colouring_image_2.png # size:  111434
convert json/images_chatbot/Counting_Squares_image_0.png -resize 50% json/images_chatbot/Counting_Squares_image_0.png # size:   28323
convert json/images_chatbot/Counting_Squares_image_1.png -resize 45% json/images_chatbot/Counting_Squares_image_1.png # size:   18486
convert json/images_chatbot/Counting_Squares_image_2.png -resize 50% json/images_chatbot/Counting_Squares_image_2.png # size:   25606
convert json/images_chatbot/Fifteen_image_0.png -resize 20% -background white -alpha remove json/images_chatbot/Fifteen_image_0.png # size:   64534
convert json/images_chatbot/Four_Colours_image_0.png -resize 25% json/images_chatbot/Four_Colours_image_0.png # size:  207338
convert json/images_chatbot/Four_Colours_image_1.png -resize 25% json/images_chatbot/Four_Colours_image_1.png # size:  226959
convert json/images_chatbot/Four_Colours_image_2.png -resize 25% json/images_chatbot/Four_Colours_image_2.png # size:   56308
convert json/images_chatbot/Four_Colours_image_3.png -resize 25% json/images_chatbot/Four_Colours_image_3.png # size:  111030
convert json/images_chatbot/Going_to_School_image_0.png -resize 60% json/images_chatbot/Going_to_School_image_0.png # size:    8817
convert json/images_chatbot/House_image_0.png -resize 35% json/images_chatbot/House_image_0.png # size:   63369
convert json/images_chatbot/House_image_1.png -resize 35% json/images_chatbot/House_image_1.png # size:   70960
convert json/images_chatbot/House_image_2.png -resize 60% json/images_chatbot/House_image_2.png # size:   11419
convert json/images_chatbot/Newspaper_image_0.png -resize 50% json/images_chatbot/Newspaper_image_0.png # size:   12981
convert json/images_chatbot/Pieces_of_Cake_image_0.png -resize 50% json/images_chatbot/Pieces_of_Cake_image_0.png # size:   39698
convert json/images_chatbot/Pong_Hau_K_i_image_0.png -resize 25% json/images_chatbot/Pong_Hau_K_i_image_0.png # size:   80189
# convert json/images_chatbot/Pong_Hau_K_i_image_1.png -resize 50% json/images_chatbot/Pong_Hau_K_i_image_1.png # size:   14250
convert json/images_chatbot/Pong_Hau_K_i_image_2.png -resize 40% json/images_chatbot/Pong_Hau_K_i_image_2.png # size:   21811
# convert json/images_chatbot/Square_Numbers_and_Triangular_Numbers_image_0.png -resize 50% json/images_chatbot/Square_Numbers_and_Triangular_Numbers_image_0.png # size:   19794
# convert json/images_chatbot/Square_Numbers_and_Triangular_Numbers_image_1.png -resize 50% json/images_chatbot/Square_Numbers_and_Triangular_Numbers_image_1.png # size:   18017
# convert json/images_chatbot/Square_Numbers_and_Triangular_Numbers_image_2.png -resize 50% json/images_chatbot/Square_Numbers_and_Triangular_Numbers_image_2.png # size:    8154
convert json/images_chatbot/Table_Handshakes_image_0.png -resize 50% json/images_chatbot/Table_Handshakes_image_0.png # size:   12920
convert json/images_chatbot/Table_Handshakes_image_1.png -resize 50% json/images_chatbot/Table_Handshakes_image_1.png # size:   20814
convert json/images_chatbot/Table_Handshakes_image_2.png -resize 50% json/images_chatbot/Table_Handshakes_image_2.png # size:   20385
convert json/images_chatbot/Table_Handshakes_image_3.png -resize 50% json/images_chatbot/Table_Handshakes_image_3.png # size:   16475
convert json/images_chatbot/Table_Handshakes_image_4.png -resize 50% json/images_chatbot/Table_Handshakes_image_4.png # size:   25301
convert json/images_chatbot/Triangular_Slices_image_0.png -resize 20% json/images_chatbot/Triangular_Slices_image_0.png # size:   62312
convert json/images_chatbot/Triangular_Slices_image_1.png -resize 50% json/images_chatbot/Triangular_Slices_image_1.png # size:    5947
# convert json/images_chatbot/Triangular_Slices_image_2.png -resize 50% json/images_chatbot/Triangular_Slices_image_2.png # size:   13021
# convert json/images_chatbot/Triangular_Slices_image_3.png -resize 50% json/images_chatbot/Triangular_Slices_image_3.png # size:   25091
# convert json/images_chatbot/Two_Distances_image_0.png -resize 70% json/images_chatbot/Two_Distances_image_0.png # size:    7968
convert json/images_chatbot/Two_Distances_image_1.png -resize 30% json/images_chatbot/Two_Distances_image_1.png # size:  107786
# convert json/images_chatbot/Two_Distances_image_2.png -resize 70% json/images_chatbot/Two_Distances_image_2.png # size:   31305

optipng -o3 -quiet json/images_chatbot/*.png
