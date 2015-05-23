# -*- coding: cp936 -*-
# Generated from java-escape by ANTLR 4.5
from antlr4 import *
import copy
import sys

# This class defines a complete listener for a parse tree produced by rp2cParser.
class rp2cListener(ParseTreeListener):
    __id_list = []
    __id_type = ""
    __id_range_low = 0
    __id_range_high = 0
    __sym_table = []
    __sym_table_temp = []
    __temp = {}
    __depth = 0;
    __start_sub = 0;
    __expression = ""
    __simple_expr = ""
    __term = ""
    __factor = ""


    def check_repetition(self, ID):
        temp = self.__sym_table;
        for i in range(self.__depth):
            temp = temp[-1]["list"];
            #print temp
        for i in temp:
            if i["name"] == ID : return False;
        return True
        pass

    def table_insert(self, sym):
        temp = self.__sym_table;
        for i in range(self.__depth):
            temp = temp[-1]["list"];
            #print temp
        temp.append(sym.copy());
        

    # Enter a parse tree produced by rp2cParser#program.
    def enterProgram(self, ctx):
        print "#include <stdio.h>"
        print "#include <stdlib.h>"
        pass

    # Exit a parse tree produced by rp2cParser#program.
    def exitProgram(self, ctx):
        pass


    # Enter a parse tree produced by rp2cParser#program_head.
    def enterProgram_head(self, ctx):
        pass

    # Exit a parse tree produced by rp2cParser#program_head.
    def exitProgram_head(self, ctx):
        pass


    # Enter a parse tree produced by rp2cParser#identifier_list.
    def enterIdentifier_list(self, ctx):
        #print dir(ctx)
        if "ID" in dir(ctx):
            self.__id_list.append( ctx.ID().getText() )
        pass

    # Exit a parse tree produced by rp2cParser#identifier_list.
    def exitIdentifier_list(self, ctx):
        pass


    # Enter a parse tree produced by rp2cParser#program_body.
    def enterProgram_body(self, ctx):
        self.__level = 0;
        pass

    # Exit a parse tree produced by rp2cParser#program_body.
    def exitProgram_body(self, ctx):
        pass


    # Enter a parse tree produced by rp2cParser#declarations.
    def enterDeclarations(self, ctx):
        pass

    # Exit a parse tree produced by rp2cParser#declarations.
    def exitDeclarations(self, ctx):
        #print self.__sym_table
        pass

    # Enter a parse tree produced by rp2cParser#declaration.
    def enterDeclaration(self, ctx):
        del self.__id_list[0:]
        pass

    # Exit a parse tree produced by rp2cParser#declaration.
    def exitDeclaration(self, ctx):
        del self.__id_list[0:]
        pass


    # Enter a parse tree produced by rp2cParser#type_.
    def enterType_(self, ctx):
        #print dir(ctx)
        if ctx.getChildCount() == 1: #standard_type
            pass
        elif ctx.getChildCount() == 3: #record_type
            
            for i in range(len(self.__id_list)):
                if not self.check_repetition(self.__id_list[i].encode()):
                    print >>sys.stderr,"�ظ�����:", self.__id_list[i].encode(), ";before:", ctx.getText()
                    self.__id_list.pop(i)
            if len(self.__id_list) != 0:
                for i in range(len(self.__id_list)):
                    self.__id_list[i] = self.__id_list[i].encode()
                self.__temp.clear()
                self.__temp["name"] = tuple(copy.deepcopy(self.__id_list))
                self.__temp["type"] = "struct"
                self.__temp["list"] = []
                if self.__depth == 0:
                    self.__sym_table.append(self.__temp.copy())
                else:
                    self.table_insert(self.__temp)
                self.__depth += 1;
                print "struct",
                print self.__id_list[0],
                for i in self.__id_list[1:]:
                    print ',' , i,
                print "{"
            
        elif ctx.getChildCount() == 7:
            self.__id_range_high = int(ctx.DIGITS()[1].getText())
            self.__id_range_low = int(ctx.DIGITS()[0].getText())
            #array_type
        pass

    # Exit a parse tree produced by rp2cParser#type_.
    def exitType_(self, ctx):
        #print dir(ctx)
        if ctx.getChildCount() == 7 : ## array type
            for i in range(len(self.__id_list)):
                if not self.check_repetition(self.__id_list[i].encode()):
                    print >>sys.stderr,"�ظ�����:", self.__id_list[i].encode(), ";before:", ctx.getText()
                    self.__id_list.pop(i)
            if len(self.__id_list) != 0:
                print self.__id_type,
                for i in self.__id_list[0:1]: print "%s[%d]" %(i, self.__id_range_high+1), 
                for i in self.__id_list[1:]:
                    print ",%s[%d]" %(i, self.__id_range_high+1),
                print ';'

                for i in self.__id_list: ##insert in symbol table
                    self.__temp.clear()
                    self.__temp["name"] = i.encode()
                    self.__temp["type"] = self.__id_type
                    self.__temp["range_high"] = self.__id_range_high
                    self.__temp["range_low"] = self.__id_range_low
                    if self.__depth == 0:
                        self.__sym_table.append(self.__temp.copy())
                    else:
                        self.table_insert(self.__temp)
                
        elif ctx.getChildCount() == 1: ## standard type
            for i in range(len(self.__id_list)):
                if not self.check_repetition(self.__id_list[i].encode()):
                    print >>sys.stderr,"�ظ�����:", self.__id_list[i].encode(), ";before:", ctx.getText()
                    self.__id_list.pop(i)
            if len(self.__id_list) != 0:
                
                print self.__id_type,
                for i in self.__id_list[0:1]: print i,
                for i in self.__id_list[1:]:
                    print ',' , i,
                print ';'
                
                for i in self.__id_list: ##insert in symbol table
                    self.__temp.clear()
                    self.__temp["name"] = i.encode()
                    self.__temp["type"] = self.__id_type
                    if self.__depth == 0:
                        self.__sym_table.append(self.__temp.copy())
                    else:
                        self.table_insert(self.__temp)
                    
                
        if ctx.getChildCount() == 3:
                
            self.__depth -= 1;
            print "}" ##���ף���������ν��:)
        pass


    # Enter a parse tree produced by rp2cParser#standard_type.
    def enterStandard_type(self, ctx):
        pass

    # Exit a parse tree produced by rp2cParser#standard_type.
    def exitStandard_type(self, ctx):
        if ctx.getText() == "integer":
            self.__id_type = "int"
        elif ctx.getText() == "real":
            self.__id_type = "double"
        elif ctx.getText() == "Boolean":
            self.__id_type = "int"
        pass


    # Enter a parse tree produced by rp2cParser#subprogram_declarations.
    def enterSubprogram_declarations(self, ctx):
        pass

    # Exit a parse tree produced by rp2cParser#subprogram_declarations.
    def exitSubprogram_declarations(self, ctx):
        pass


    # Enter a parse tree produced by rp2cParser#subprogram_declaration.
    def enterSubprogram_declaration(self, ctx):
        #self.__sym_table.append([].copy()) 
        pass

    # Exit a parse tree produced by rp2cParser#subprogram_declaration.
    def exitSubprogram_declaration(self, ctx):
        #print "int main()"
        self.__depth -= 1;

    # Enter a parse tree produced by rp2cParser#subprogram_head.
    def enterSubprogram_head(self, ctx):
        self.__start_sub = 0; 
        if ctx.getChildCount() == 6: #function
            self.__temp.clear()
            self.__temp["name"] = ctx.ID().getText().encode()
            self.__temp["type"] = "function"
            self.__temp["list"] = []
            self.__temp["return_type"] = self.__id_type
            self.__sym_table.append(self.__temp.copy())
            self.__depth += 1;
            print self.__id_type,
            print "%s(" %self.__temp["name"],
            pass
        elif ctx.getChildCount() == 4 : #proceudre
            pass
        pass

    # Exit a parse tree produced by rp2cParser#subprogram_head.
    def exitSubprogram_head(self, ctx):
        #print dir(ctx)
        pass


    # Enter a parse tree produced by rp2cParser#arguments.
    def enterArguments(self, ctx):
        pass

    # Exit a parse tree produced by rp2cParser#arguments.
    def exitArguments(self, ctx):
        print ')'
        pass


    # Enter a parse tree produced by rp2cParser#parameter_lists.
    def enterParameter_lists(self, ctx):
        pass

    # Exit a parse tree produced by rp2cParser#parameter_lists.
    def exitParameter_lists(self, ctx):
        pass


    # Enter a parse tree produced by rp2cParser#parameter_list.
    def enterParameter_list(self, ctx):
        del self.__id_list[0:]
        pass

    # Exit a parse tree produced by rp2cParser#parameter_list.
    def exitParameter_list(self, ctx):
        if ctx.getChildCount() == 3:
            self.__id_list.reverse()
            for i in self.__id_list:
                self.__temp["name"] = i.encode()
                self.__temp["type"] = self.__id_type
                self.table_insert(self.__temp)
            for i in self.__id_list:
                if self.__start_sub == 0:
                    self.__start_sub = 1;
                    print self.__temp["type"], i,
                else:
                    print ',%s' %self.__temp["type"], i,
            pass
        elif ctx.getChildCount() == 4:
            for i in self.__id_list:
                self.__temp["name"] = i.encode()
                self.__temp["type"] = self.__id_type
                self.__temp["option"] = "VAR"
                self.table_insert(self.__temp)
            pass
        pass


    # Enter a parse tree produced by rp2cParser#compound_statement.
    def enterCompound_statement(self, ctx):
        print '{'
        pass

    # Exit a parse tree produced by rp2cParser#compound_statement.
    def exitCompound_statement(self, ctx):
        print '}'
        pass


    # Enter a parse tree produced by rp2cParser#optional_statements.
    def enterOptional_statements(self, ctx):
        pass

    # Exit a parse tree produced by rp2cParser#optional_statements.
    def exitOptional_statements(self, ctx):
        pass


    # Enter a parse tree produced by rp2cParser#statement_list.
    def enterStatement_list(self, ctx):
        pass

    # Exit a parse tree produced by rp2cParser#statement_list.
    def exitStatement_list(self, ctx):
        pass


    # Enter a parse tree produced by rp2cParser#statement.
    def enterStatement(self, ctx):
        if "ASSIGNOP" in dir(ctx):
            print ctx.variable().ID().getText().encode(),
            print '=',
            print 
            pass
        print dir(ctx)
        pass

    # Exit a parse tree produced by rp2cParser#statement.
    def exitStatement(self, ctx):
        if "ASSIGNOP" in dir(ctx):
            pass
        pass


    # Enter a parse tree produced by rp2cParser#variable.
    def enterVariable(self, ctx):
        pass

    # Exit a parse tree produced by rp2cParser#variable.
    def exitVariable(self, ctx):
        pass


    # Enter a parse tree produced by rp2cParser#procedure_call_statement.
    def enterProcedure_call_statement(self, ctx):
        pass

    # Exit a parse tree produced by rp2cParser#procedure_call_statement.
    def exitProcedure_call_statement(self, ctx):
        pass


    # Enter a parse tree produced by rp2cParser#expr_list.
    def enterExpr_list(self, ctx):
        pass

    # Exit a parse tree produced by rp2cParser#expr_list.
    def exitExpr_list(self, ctx):
        pass


    # Enter a parse tree produced by rp2cParser#expression.
    def enterExpression(self, ctx):
        pass

    # Exit a parse tree produced by rp2cParser#expression.
    def exitExpression(self, ctx):
        pass


    # Enter a parse tree produced by rp2cParser#simple_expr.
    def enterSimple_expr(self, ctx):
        pass

    # Exit a parse tree produced by rp2cParser#simple_expr.
    def exitSimple_expr(self, ctx):
        pass


    # Enter a parse tree produced by rp2cParser#term.
    def enterTerm(self, ctx):
        pass

    # Exit a parse tree produced by rp2cParser#term.
    def exitTerm(self, ctx):
        pass


    # Enter a parse tree produced by rp2cParser#factor.
    def enterFactor(self, ctx):
        pass

    # Exit a parse tree produced by rp2cParser#factor.
    def exitFactor(self, ctx):
        pass


    # Enter a parse tree produced by rp2cParser#sign.
    def enterSign(self, ctx):
        pass

    # Exit a parse tree produced by rp2cParser#sign.
    def exitSign(self, ctx):
        pass

