'''
XML2Py - XML to Python de-serialization

This code transforms an XML document into a Python data structure

Usage:
    deserializer = XML2Py()
    python_object = deserializer.parse( xml_string )
    print xml_string
    print python_object
'''

from lxml import etree
from pathlib import Path
from xml.etree import ElementTree as ET

class XML2Py():

    def __init__( self ):

        self._parser = parser = etree.XMLParser( remove_blank_text=True )
        self._root = None  # root of etree structure
        self.data = None   # where we store the processed Python structure

    def parse( self, xmlString ):
        '''
        processes XML string into Python data structure
        '''
        self._root = etree.fromstring( xmlString, self._parser )
        self.data = self._parseXMLRoot()
        return self.data

    def tostring( self ):
        '''
        creates a string representation using our etree object
        '''
        if self._root != None:
            return etree.tostring( self._root )

    def _parseXMLRoot( self ):
        '''
        starts processing, takes care of first level idisyncrasies
        '''
        childDict = self._parseXMLNode( self._root )
        return { self._root.tag : childDict["children"] }

    def _parseXMLNode( self, element ):
        '''
        rest of the processing
        '''
        childContainer = None # either Dict or List

        # process any tag attributes
        # if we have attributes then the child container is a Dict
        #   otherwise a List
        if element.items():
            childContainer = {}
            childContainer.update( dict( element.items() ) )
        else:
            childContainer = []


        if isinstance( childContainer, list ) and element.text:
            # tag with no attributes and one that contains text
            childContainer.append( element.text )

        else:
            # tag might have children, let's process them
            for child_elem in element.getchildren():

                childDict = self._parseXMLNode( child_elem )

              # let's store our child based on container type
                #
                if isinstance( childContainer, dict ):
                    # these children are lone tag entities ( eg, 'copyright' )
                    childContainer.update( { childDict["tag"] : childDict["children"] } )

                else:
                    # these children are repeated tag entities ( eg, 'format' )
                    childContainer.append( childDict["children"] )

        return { "tag":element.tag, "children": childContainer }


def main():

    xml_string = '''
    <map title="cfa21" id="2021_cfa_l1_mod_quizzes">
   <topichead navtitle="Ethical and Professional Standards">
      <topichead navtitle="Study Session 1: Ethical and Professional Standards">
         <topichead navtitle="Reading 1: Ethics and Trust in the Investment Profession">
            <topicref href="questions/cfaL1_assessoverview_quiz_m1.dita"/>
         </topichead>
         <topichead navtitle="Reading 2: Code of Ethics and Standards of Professional Conduct">
            <topicref href="questions/cfaL1_assessoverview_quiz_m2.dita"/>
         </topichead>
         <topichead navtitle="Reading 3: Guidance for Standards I–VII">
            <topicref href="questions/cfaL1_assessoverview_quiz_m3.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m6.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m8.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m10.dita"/>
         </topichead>
         <topichead navtitle="Reading 4: Introduction to the Global Investment Performance Standards (GIPS®)">
            <topicref href="questions/cfaL1_assessoverview_quiz_m12.dita"/>
         </topichead>
         <topichead navtitle="Reading 5: Global Investment Performance Standards (GIPS®)">
            <topicref href="questions/cfaL1_assessoverview_quiz_m13.dita"/>
         </topichead>
      </topichead>
   </topichead>
   <topichead navtitle="Quantitative Methods">
      <topichead navtitle="Study Session 2: Quantitative Methods (1)">
         <topichead navtitle="Reading 6: The Time Value of Money">
            <topicref href="questions/cfaL1_assessoverview_quiz_m14.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m15.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m16.dita"/>
         </topichead>
         <topichead navtitle="Reading 7: Statistical Concepts and Market Returns">
            <topicref href="questions/cfaL1_assessoverview_quiz_m19.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m20.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m21.dita"/>
         </topichead>
         <topichead navtitle="Reading 8: Probability Concepts">
            <topicref href="questions/cfaL1_assessoverview_quiz_m22.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m23.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m24.dita"/>
         </topichead>
      </topichead>
      <topichead navtitle="Study Session 3: Quantitative Methods (2)">
         <topichead navtitle="Reading 9: Common Probability Distributions">
            <topicref href="questions/cfaL1_assessoverview_quiz_m25.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m26.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m27.dita"/>
         </topichead>
         <topichead navtitle="Reading 10: Sampling and Estimation">
            <topicref href="questions/cfaL1_assessoverview_quiz_m28.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m29.dita"/>
         </topichead>
         <topichead navtitle="Reading 11: Hypothesis Testing">
            <topicref href="questions/cfaL1_assessoverview_quiz_m30.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m31.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m32.dita"/>
         </topichead>
      </topichead>
   </topichead>
   <topichead navtitle="Economics">
      <topichead navtitle="Study Session 4: Economics (1)">
         <topichead navtitle="Reading 12: Topics in Demand and Supply Analysis">
            <topicref href="questions/cfaL1_assessoverview_quiz_m34.dita"/>
         </topichead>
         <topichead navtitle="Reading 13: The Firm and Market Structures">
            <topicref href="questions/cfaL1_assessoverview_quiz_m36.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m37.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m38.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m39.dita"/>
         </topichead>
         <topichead navtitle="Reading 14: Aggregate Output, Prices, and Economic Growth">
            <topicref href="questions/cfaL1_assessoverview_quiz_m40.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m41.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m42.dita"/>
         </topichead>
         <topichead navtitle="Reading 15: Understanding Business Cycles">
            <topicref href="questions/cfaL1_assessoverview_quiz_m43.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m44.dita"/>
         </topichead>
      </topichead>
      <topichead navtitle="Study Session 5: Economics (2)">
         <topichead navtitle="Reading 16: Monetary and Fiscal Policy">
            <topicref href="questions/cfaL1_assessoverview_quiz_m45.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m46.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m47.dita"/>
         </topichead>
         <topichead navtitle="Reading 17: International Trade and Capital Flows">
            <topicref href="questions/cfaL1_assessoverview_quiz_m48.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m49.dita"/>
         </topichead>
         <topichead navtitle="Reading 18: Currency Exchange Rates">
            <topicref href="questions/cfaL1_assessoverview_quiz_m50.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m51.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m52.dita"/>
         </topichead>
      </topichead>
   </topichead>
   <topichead navtitle="Financial Reporting and Analysis">
      <topichead navtitle="Study Session 6: Financial Reporting and Analysis (1)">
         <topichead navtitle="Reading 19: Introduction to Financial Statement Analysis">
            <topicref href="questions/cfaL1_assessoverview_quiz_m53.dita"/>
         </topichead>
         <topichead navtitle="Reading 20: Financial Reporting Standards">
            <topicref href="questions/cfaL1_assessoverview_quiz_m55.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m56.dita"/>
         </topichead>
      </topichead>
      <topichead navtitle="Study Session 7: Financial Reporting and Analysis (2)">
         <topichead navtitle="Reading 21: Understanding Income Statements">
            <topicref href="questions/cfaL1_assessoverview_quiz_m58.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m61.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m62.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m63.dita"/>
         </topichead>
         <topichead navtitle="Reading 22: Understanding Balance Sheets">
            <topicref href="questions/cfaL1_assessoverview_quiz_m64.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m66.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m68.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m70.dita"/>
         </topichead>
         <topichead navtitle="Reading 23: Understanding Cash Flow Statements">
            <topicref href="questions/cfaL1_assessoverview_quiz_m71.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m72.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m73.dita"/>
         </topichead>
         <topichead navtitle="Reading 24: Financial Analysis Techniques">
            <topicref href="questions/cfaL1_assessoverview_quiz_m75.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m78.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m79.dita"/>
         </topichead>
      </topichead>
      <topichead navtitle="Study Session 8: Financial Reporting and Analysis (3)">
         <topichead navtitle="Reading 25: Inventories">
            <topicref href="questions/cfaL1_assessoverview_quiz_m80.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m81.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m82.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m83.dita"/>
         </topichead>
         <topichead navtitle="Reading 26: Long-Lived Assets">
            <topicref href="questions/cfaL1_assessoverview_quiz_m85.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m86.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m87.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m88.dita"/>
         </topichead>
         <topichead navtitle="Reading 27: Income Taxes">
            <topicref href="questions/cfaL1_assessoverview_quiz_m89.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m91.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m93.dita"/>
         </topichead>
         <topichead navtitle="Reading 28: Non-Current (Long-Term) Liabilities">
            <topicref href="questions/cfaL1_assessoverview_quiz_m94.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m96.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m97.dita"/>
         </topichead>
      </topichead>
      <topichead navtitle="Study Session 9: Financial Reporting and Analysis (4)">
         <topichead navtitle="Reading 29: Financial Reporting Quality">
            <topicref href="questions/cfaL1_assessoverview_quiz_m100.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m101.dita"/>
         </topichead>
         <topichead navtitle="Reading 30: Applications of Financial Statement Analysis">
            <topicref href="questions/cfaL1_assessoverview_quiz_m103.dita"/>
         </topichead>
      </topichead>
   </topichead>
   <topichead navtitle="Corporate Finance">
      <topichead navtitle="Study Session 10: Corporate Finance (1)">
         <topichead navtitle="Reading 31: Introduction to Corporate Governance and Other ESG Considerations">
            <topicref href="questions/cfaL1_assessoverview_quiz_m105.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m106.dita"/>
         </topichead>
         <topichead navtitle="Reading 32: Capital Budgeting">
            <topicref href="questions/cfaL1_assessoverview_quiz_m107.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m108.dita"/>
         </topichead>
         <topichead navtitle="Reading 33: Cost of Capital">
            <topicref href="questions/cfaL1_assessoverview_quiz_m109.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m110.dita"/>
         </topichead>
      </topichead>
      <topichead navtitle="Study Session 11: Corporate Finance (2)">
         <topichead navtitle="Reading 34: Measures of Leverage">
            <topicref href="questions/cfaL1_assessoverview_quiz_m111.dita"/>
         </topichead>
         <topichead navtitle="Reading 35: Working Capital Management">
            <topicref href="questions/cfaL1_assessoverview_quiz_m112.dita"/>
         </topichead>
      </topichead>
   </topichead>
   <topichead navtitle="Equity Investments">
      <topichead navtitle="Study Session 12: Equity Investments (1)">
         <topichead navtitle="Reading 36: Market Organization and Structure">
            <topicref href="questions/cfaL1_assessoverview_quiz_m123.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m125.dita"/>
         </topichead>
         <topichead navtitle="Reading 37: Security Market Indexes">
            <topicref href="questions/cfaL1_assessoverview_quiz_m126.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m127.dita"/>
         </topichead>
         <topichead navtitle="Reading 38: Market Efficiency">
            <topicref href="questions/cfaL1_assessoverview_quiz_m128.dita"/>
         </topichead>
      </topichead>
      <topichead navtitle="Study Session 13: Equity Investments (2)">
         <topichead navtitle="Reading 39: Overview of Equity Securities">
            <topicref href="questions/cfaL1_assessoverview_quiz_m129.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m130.dita"/>
         </topichead>
         <topichead navtitle="Reading 40: Introduction to Industry and Company Analysis">
            <topicref href="questions/cfaL1_assessoverview_quiz_m131.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m132.dita"/>
         </topichead>
         <topichead navtitle="Reading 41: Equity Valuation: Concepts and Basic Tools">
            <topicref href="questions/cfaL1_assessoverview_quiz_m133.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m134.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m135.dita"/>
         </topichead>
      </topichead>
   </topichead>
   <topichead navtitle="Fixed Income">
      <topichead navtitle="Study Session 14: Fixed Income (1)">
         <topichead navtitle="Reading 42: Fixed-Income Securities: Defining Elements">
            <topicref href="questions/cfaL1_assessoverview_quiz_m136.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m137.dita"/>
         </topichead>
         <topichead navtitle="Reading 43: Fixed-Income Markets: Issuance, Trading, and Funding">
            <topicref href="questions/cfaL1_assessoverview_quiz_m138.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m139.dita"/>
         </topichead>
         <topichead navtitle="Reading 44: Introduction to Fixed-Income Valuation">
            <topicref href="questions/cfaL1_assessoverview_quiz_m140.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m141.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m142.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m143.dita"/>
         </topichead>
         <topichead navtitle="Reading 45: Introduction to Asset-Backed Securities">
            <topicref href="questions/cfaL1_assessoverview_quiz_m145.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m146.dita"/>
         </topichead>
      </topichead>
      <topichead navtitle="Study Session 15: Fixed Income (2)">
         <topichead navtitle="Reading 46: Understanding Fixed-Income Risk and Return">
            <topicref href="questions/cfaL1_assessoverview_quiz_m147.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m148.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m149.dita"/>
         </topichead>
         <topichead navtitle="Reading 47: Fundamentals of Credit Analysis">
            <topicref href="questions/cfaL1_assessoverview_quiz_m150.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m151.dita"/>
         </topichead>
      </topichead>
   </topichead>
   <topichead navtitle="Derivatives">
      <topichead navtitle="Study Session 16: Derivatives">
         <topichead navtitle="Reading 48: Derivative Markets and Instruments">
            <topicref href="questions/cfaL1_assessoverview_quiz_m152.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m153.dita"/>
         </topichead>
         <topichead navtitle="Reading 49: Basics of Derivative Pricing and Valuation">
            <topicref href="questions/cfaL1_assessoverview_quiz_m154.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m155.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m156.dita"/>
         </topichead>
      </topichead>
   </topichead>
   <topichead navtitle="Alternative Investments">
      <topichead navtitle="Study Session 17: Alternative Investments">
         <topichead navtitle="Reading 50: Introduction to Alternative Investments">
            <topicref href="questions/cfaL1_assessoverview_quiz_m158.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m159.dita"/>
         </topichead>
      </topichead>
   </topichead>
   <topichead navtitle="Portfolio Management">
      <topichead navtitle="Study Session 18: Portfolio Management (1)">
         <topichead navtitle="Reading 51: Portfolio Management: An Overview">
            <topicref href="questions/cfaL1_assessoverview_quiz_m113.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m114.dita"/>
         </topichead>
         <topichead navtitle="Reading 52: Portfolio Risk and Return: Part I">
            <topicref href="questions/cfaL1_assessoverview_quiz_m115.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m117.dita"/>
         </topichead>
         <topichead navtitle="Reading 53: Portfolio Risk and Return: Part II">
            <topicref href="questions/cfaL1_assessoverview_quiz_m118.dita"/>
            <topicref href="questions/cfaL1_assessoverview_quiz_m119.dita"/>
         </topichead>
      </topichead>
      <topichead navtitle="Study Session 19: Portfolio Management (2)">
         <topichead navtitle="Reading 54: Basics of Portfolio Planning and Construction">
            <topicref href="questions/cfaL1_assessoverview_quiz_m120.dita"/>
         </topichead>
         <topichead navtitle="Reading 55: Introduction to Risk Management">
            <topicref href="questions/cfaL1_assessoverview_quiz_m121.dita"/>
         </topichead>
         <topichead navtitle="Reading 56: Technical Analysis">
            <topicref href="questions/cfaL1_assessoverview_quiz_m33.dita"/>
         </topichead>
         <topichead navtitle="Reading 57: Fintech in Investment Management">
            <topicref href="questions/cfaL1_assessoverview_quiz_m122.dita"/>
         </topichead>
      </topichead>
   </topichead>
</map>
    '''
    base_path = Path(__file__).parent
    file_path = (base_path / "sampleFiles/mcqFiles/toc.ditamap").resolve()
    

    tree = ET.parse(file_path)
    root = tree.getroot()
    #xml_string = ET.tostring(root,encoding='utf8', method='xml')


    deserializer = XML2Py()
    python_object = deserializer.parse(xml_string)
    print (xml_string)
    print (python_object)


if __name__ == '__main__':
    main()