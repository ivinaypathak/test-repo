
# READING FROM FILE

# Creating file object requires manual closing the file object
# file = open('sample.txt', 'r')

#-------------------------------------------------------------------------------------------------------#

# This will automatically close the file object as you are out of scope

# with open('read_sample.txt', 'r') as file:
# 	for line in file:
#     		print(line)

# f.read() - Reads All Content In File
# f.readline() - Reads a single line
# f.readlines() - Reads all lines at one go

#-------------------------------------------------------------------------------------------------------#

# print(file.read())       			# It will read the all content and print it as it is
# print(file.read(int no_of_characters))  	# It will read the number of characters passed as argument
# print(file.readlines())  			# It will read all the lines in file and prints an array of string
# print(file.readline(), end='')   		# It will read the first line in file
# print(file.readline(), end='')   		# It will read the second line in file

#-------------------------------------------------------------------------------------------------------#

# size_to_read = 10

# content = file.read(size_to_read)
# print(content)
# print(file.tell())     			 # Tell the current position of the cursor being held
# file.seek(0)             			 # Makes the cursor to reach at the beginning of the file

# content = file.read(size_to_read)
# print(content)

# while len(content) > 0:
#     print(content)
#     content = file.read(size_to_read)
# print(len(content))

# print(file.mode)
# print(file.name)

# file.close()

#-------------------------------------------------------------------------------------------------------#

# WRITING TO FILE

# If file already exists.It will overwrite the content in file
# If file does not exists.It will create the file and write to the file.
# with open('read_sample.txt', 'r') as read_file:
#     with open('write_sample.txt', 'w') as write_file:
# file.write('This is Vinay Pathak')
# file.seek(0)
# write_file.write(read_file.read())        	     # Reading from the read file and writing it to the write file


# READING AND WRITING TO BINARY FILES
# Making copy of the alogorithms jpg file
with open('algorithms.jpg', 'rb') as read_binary:
    with open('algorithms_copy_copy.jpg', 'wb') as write_binary:
        # write_binary.write(read_binary.read())

        # Reading and writing into file in chunks
        chunk_size = 421
        read_binary_chunk = read_binary.read(chunk_size)
        while len(read_binary_chunk) > 0:
            write_binary.write(read_binary_chunk)
            read_binary_chunk = read_binary.read(chunk_size)
#-------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#
