// Gene2DArray.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

//File Reading, etc
#include <iostream>
#include <iomanip>
#include <string.h>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <sstream>
#include <vector>

//OpenGL
#include <gl/glut.h>
#include <gl/GLU.h>

//Autonomously Defined Class
#include "Gene.h"

using namespace std;


//__________________Globals______________//

int win;
//Since this software program will be run on a per cluster file basis,
//the number of genes in the text file's cluster can be represented as a global variable
int totalGenes;
vector<pair <string, double> > geneVect;
int drawCounter = 0;
ifstream fileStream;




//--------------------Input Cluster Text File--------------------//
//Function Prototypes for this section:

vector<pair <string,double> > getGenes();

int getGeneCount();

void fileInfoDraw();

//
//Constructs a vector structure that contains vectors of gene pairs.
//Requires an appropriately formatted text file
//
vector<pair <string,double> > getGenes()
{
	vector<pair <string, double> > genevect;
	string line;
	getline(fileStream, line);
    cout << "Genes and representations read from the text file:\n";
	while (fileStream.good())
	{
		getline (fileStream, line); 
		pair<string, double> pair;
		unsigned long split = line.find("\t");
		string gene = line.substr(0, split);
		string num = line.substr(split + 1);
		double geneNum = atof(num.c_str());
		pair.first = gene;
		pair.second = geneNum;
		genevect.push_back(pair);
		cout << gene + " " + num << endl;
	}
	return genevect;
}

//
//Finds the total gene count of the input .txt file.
//
int getGeneCount()
{
	// read the first line
	string firstLine;
	getline (fileStream, firstLine);
	
	// find the position of the string
	unsigned long pos = firstLine.find(": ");
	// put the number into a string
	string number = firstLine.substr(pos + 2);
	// convert to integer
	int count = atoi(number.c_str());
    
    return count;
}

//A gene cluster .txt file of the specified format is fed into this function.
//The cluster file is read line by line, separating the genes from their expression data and assigning them to distinct named variables. 
//The data will be used to set the total gene count and create a vector structure containing vector pairs of gene names and expressions ratios.
void fileInfoDraw(){
    // opens the file
    //**Set the path to reach the text file you wish to implement
	//fileStream.open("./TextFiles/Cerevisiae_heatShock.txt"); 
	//fileStream.open("./TextFiles/Cerevisiae_stressResponse.txt"); 
	fileStream.open("./TextFiles/Cerevisiae_oxidativeResponse.txt");
	//fileStream.open("./TextFiles/Cerevisiae_transcriptionFactor.txt");
	if (!fileStream){
		cout << "Unable to open file";
        exit(1); // terminate with error
	}
    
//GLOBAL variables set here.
    totalGenes = getGeneCount();
	geneVect = getGenes();
}

//_____________________________Drawing Code_________________________________________//

void drawGene(int x, int y, int expressionHeight, bool repressed){

	//Not repressed = red
	glColor3f(0.9f, 0.3f, 0.3f);

	if (repressed){
		//Repressed = green
		glColor3f(0.0f, 1.0f, 0.3f);
	}
    
    glVertex2d( x, y);
    glVertex2d( x, y + expressionHeight);
    glVertex2d( x + 5, y + expressionHeight);
    glVertex2d( x + 5 , y);

}

void drawScene(){
    
    //***Number of rows to draw to the Y axis
    int numRows = 2;
    //***Number of genes per row
    int numRowGenes = 7;

	//Margins
	int marginX = 50;
	int marginY = 50;

	//Spacing
	int spacingX = 20;
    int spacingY = 30;

    int counter = 0;

	glPushMatrix();
    glBegin(GL_QUADS);
    //Draw along the Y axis
    for (int y = marginY; y < (numRows * spacingY) + marginY;  y += spacingY){
        //Draw along the X axis
        for (int x = marginX; x < (numRowGenes * spacingX) + marginX; x += spacingX){
			if (counter < totalGenes){
				//Draw a gene from the counted index of the file information.
				Gene currentGene;
				currentGene.setGeneInformation(counter);
				drawGene( x, y, currentGene.expressionHeight, currentGene.repressed);
            
				//Increment to draw next gene
				counter++;
			}
        }
    }
    
    glEnd();
    glPopMatrix();
    
}

void renderCluster(){
     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    
    drawScene();
    
    glutSwapBuffers();

}

//--------------------Main and Fundamental Functions--------------------//
void initializeScene();
void escapeDisplay(unsigned char key, int xx, int yy);


void initializeScene(){
    
    glutKeyboardFunc(escapeDisplay);
    //glutFullScreen();
    
    //Set background to white.
    glClearColor(1.0, 1.0, 1.0, 0.0);
    
    //Set appropriate matrices.
    glMatrixMode(GL_MODELVIEW);
    
    glLoadIdentity();
    
    
    //Establish a 2Dcoordinate System
    //Compute using given algorithm, manually adjust to fit from there
    //*Could someone implement this dynamically?    
    gluOrtho2D(0, 300, 0, 200);
}

void escapeDisplay(unsigned char key, int xx, int yy){
    if (key == 27){
        glutDestroyWindow(win);
    }
}


int main (int argc, const char * argv[])
{
    
    fileInfoDraw();

    //Glut Window Initialization.
    glutInit(&argc, (char**)argv);
    glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA);
    glutInitWindowSize(640, 480);
    glutInitWindowPosition(0, 0);
    win = glutCreateWindow("RNA-seq Result Visualization");
    
    //Set up the main display window.
    initializeScene();
    
    glutFullScreen();
    
    glutDisplayFunc(renderCluster);
    
    glutMainLoop();    
	return 0;
}

