#include "StdAfx.h"
#include "Gene.h"


Gene::Gene(void)
{

	void setGeneInformation(int index){
    //Get next gene vector to draw here
    pair<string, double> geneInfo = geneVect.at(index);
    
    Gene geneToDraw;
    name = geneInfo.first; 
    expression = geneInfo.second;
    
    
    //Determine whether repressed or upregulated
    repressed = false;
    if (expression < 0.0f) {
        repressed = true;
    }
    
    //    //Determine height to represent the gene's expression.
    //    //determineExpressionHeight(expressionValue);
    //    //Draw repressed / increased expression with height bars inverted
    //    //relative to each other
    
    expressionHeight = (int)(expression * 5.0f);
    
}

