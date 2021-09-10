all: Compile Link Execute

Compile:
	g++ -c project1.cpp

Link:
	g++ project1.o -o project1.exe

Execute:
	./project1.exe
