# -*- coding: cp936 -*-
# Generated from java-escape by ANTLR 4.5
from antlr4 import *

# This class defines a complete listener for a parse tree produced by rp2cParser.
class rp2cListener(ParseTreeListener):
    __id_list = []
    __id_type = ""
    __id_range = 0
    __sym_table = []
    __level = 0;
    __temp = {}

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
            self.__id_list.append(ctx.ID().getText())
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
        print self.__sym_table
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
            print "struct",
            print self.__id_list[0],
            for i in self.__id_list[1:]:
                print ',' , i,
                
            for i in self.__id_list: ##insert in symbol table
                self.__temp.clear()
                self.__temp["name"] = i.encode()
                self.__temp["type"] = "struct"
                self.__temp["level"] = self.__level
                self.__sym_table.append(self.__temp.copy())
            print "{"
        elif ctx.getChildCount() == 7:
            self.__id_range = int(ctx.DIGITS()[1].getText()) #array_type
        pass

    # Exit a parse tree produced by rp2cParser#type_.
    def exitType_(self, ctx):
        if ctx.getChildCount() == 7 : ## array type
            print self.__id_type,
            for i in self.__id_list[0:1]: print "%s[%d]" %(i, self.__id_range+1), 
            for i in self.__id_list[1:]:
                print ",%s[%d]" %(i, self.__id_range+1),
            print ';'

            for i in self.__id_list: ##insert in symbol table
                self.__temp.clear()
                self.__temp["name"] = i.encode()
                self.__temp["type"] = self.__id_type
                self.__temp["level"] = self.__level
                self.__temp["range"] = self.__id_range+1 
                self.__sym_table.append(self.__temp.copy())
                
        elif ctx.getChildCount() == 1: ## standard type
            print self.__id_type,
            for i in self.__id_list[0:1]: print i,
            for i in self.__id_list[1:]:
                print ',' , i,
            print ';'
            
            for i in self.__id_list: ##insert in symbol table
                self.__temp.clear()
                self.__temp["name"] = i.encode()
                self.__temp["type"] = self.__id_type
                self.__temp["level"] = self.__level
                self.__sym_table.append(self.__temp.copy())

        if ctx.getChildCount() == 3:
            print "}"
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
        pass

    # Exit a parse tree produced by rp2cParser#subprogram_declaration.
    def exitSubprogram_declaration(self, ctx):
        pass


    # Enter a parse tree produced by rp2cParser#subprogram_head.
    def enterSubprogram_head(self, ctx):
        pass

    # Exit a parse tree produced by rp2cParser#subprogram_head.
    def exitSubprogram_head(self, ctx):
        pass


    # Enter a parse tree produced by rp2cParser#arguments.
    def enterArguments(self, ctx):
        pass

    # Exit a parse tree produced by rp2cParser#arguments.
    def exitArguments(self, ctx):
        pass


    # Enter a parse tree produced by rp2cParser#parameter_lists.
    def enterParameter_lists(self, ctx):
        pass

    # Exit a parse tree produced by rp2cParser#parameter_lists.
    def exitParameter_lists(self, ctx):
        pass


    # Enter a parse tree produced by rp2cParser#parameter_list.
    def enterParameter_list(self, ctx):
        pass

    # Exit a parse tree produced by rp2cParser#parameter_list.
    def exitParameter_list(self, ctx):
        pass


    # Enter a parse tree produced by rp2cParser#compound_statement.
    def enterCompound_statement(self, ctx):
        pass

    # Exit a parse tree produced by rp2cParser#compound_statement.
    def exitCompound_statement(self, ctx):
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
        pass

    # Exit a parse tree produced by rp2cParser#statement.
    def exitStatement(self, ctx):
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


