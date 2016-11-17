'''import png
f = open('../../eye_image.png', 'wb')      # binary mode is important
w = png.Writer(255, 1, greyscale=True)
w.write(f, [range(256)])
f.close()

print(w)'''


#Lab 10 Steganography
#Author: Fionn Mcguire
#Student Number: C13316356
#Date: 16/11/2016

import png, array

message = 'final security lab'
print("Plaintext: %s" %message)
binary_message = ''.join(format(ord(x), 'b') for x in message)
print("Binary Message: %s" %binary_message)
#print(len(binary_message))
#Remember to use bits, not bytes

reader = png.Reader(filename='../../eye_image.png')
w, h, pixels, metadata = reader.read_flat()
i = 0
#while i < len(binary_message):
while i < len(binary_message):
    #print(pixels[i]%2)
    #print(binary_message[i])
    p = int(pixels[i])
    #print(type(p))
    #print(type(pixels[i]))
    #print("Old: %s" % pixels[i])
    #print("Finally")
    #print(p%2)
    if p%2 == 0 and binary_message[i] == '1':
        pixels[i] = p+1
        #print('hello')
    if p%2 == 1 and binary_message[i] == '0':
        pixels[i] = p-1
        #print('hello')
    
    #old_bin_string = bin(pixels[i])
    #new_bin_string = old_bin_string[:-1].join(binary_message[i])
    #pixels[i] = int(new_bin_string,2)
    
    #print("New %s" % new_bin_string)
    #print("New Pixels %s" % pixels[i])
    i = i+1

#print(bin(pixels[0]))


output = open('../../new1_eye_image.png', 'wb')
writer = png.Writer(w, h, **metadata)
writer.write_array(output, pixels)
output.close()


reader = png.Reader(filename='../../new1_eye_image.png')
w, h, pixels, metadata = reader.read_flat()

#Return message

i = 0
new_binary_message = ''
#while i < len(binary_message):
while i < len(binary_message):
    print("Last Diget of bin string corresponds to sequential bit in binary message %s"%bin(pixels[i]))
    old_bin_string = bin(pixels[i])
    #print(pixels[i])
    pix_value = pixels[i]%2
    #print(pix_value)
    new_binary_message += `pix_value`
    i = i+1
    #print(i)
#print("New Binary %s" % new_binary_message.decode('utf-8'))
i = 0
j = 0
decrypted_message = []
for i in range(len(new_binary_message)):
       decrypted_message.append(b'')
i = 0
#print(decrypted_message)

while i < len(new_binary_message)/8:
    size = 8
    if i % size == 0 and i != 0:
        j +=1
    decrypted_message[j] = decrypted_message[j].join(new_binary_message[i])
    i +=1
#print(new_binary_message)
#print(decrypted_message)





