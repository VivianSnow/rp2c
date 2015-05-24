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
    __sub_have_decl = 0
    __variable_type = ""
    __expression_type = ""
    __simple_expr_type = ""
    __term_type = ""
    __factor_type = ""
    __have_error = 0
    __write_control_form = ""
    __if_write = 0

    def del_sub_pra(self):
        if "list" in self.__sym_table[-1]:
            if self.__sym_table[-1]["list"]:
                del self.__sym_table[-1]["list"][0:] 

    def search_sub_pra(self, ID):
        if "list" in self.__sym_table[-1]:
            for i in self.__sym_table[-1]["list"]:
                if i["name"] == ID:
                    return i
        return None

    def search_main_pra(self, ID):
        for i in self.__sym_table:
            if i["name"] == ID:
                return i
        return None

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
        print "#include <iostream>"
        print "#include <stdio.h>"
        print "#include <stdlib.h>"
        print "using namespace std;"
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
                    print >>sys.stderr,"重复定义:", self.__id_list[i].encode(), ";before:", ctx.getText()
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
                    print >>sys.stderr,"重复定义:", self.__id_list[i].encode(), ";before:", ctx.getText()
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
                    print >>sys.stderr,"重复定义:", self.__id_list[i].encode(), ";before:", ctx.getText()
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
            print "}" ##有雷，还在想如何解决:)
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
        self.__sub_have_decl = 0
        if ctx.declarations():
            self.__sub_have_decl = 1
        pass

    # Exit a parse tree produced by rp2cParser#subprogram_declaration.
    def exitSubprogram_declaration(self, ctx):
        #print "int main()"
        self.del_sub_pra()
        self.__sub_have_decl = 0
        self.__depth -= 1;

    # Enter a parse tree produced by rp2cParser#subprogram_head.
    def enterSubprogram_head(self, ctx):
        self.__start_sub = 0; 
        if ctx.getChildCount() == 6: #function
            self.__temp.clear()
            self.__temp["name"] = ctx.ID().getText().encode()
            self.__temp["type"] = "function"
            self.__temp["list"] = []
            self.__sym_table.append(self.__temp.copy())
            self.__depth += 1;
            if ctx.standard_type().getText() == "integer":
                print "int",
            elif ctx.standard_type().getText() == "real":
                print "double",
            elif ctx.standard_type().getText() == "Boolean":
                print "int",
            print "%s(" %self.__temp["name"],
            pass
        elif ctx.getChildCount() == 4 : #proceudre/
            self.__temp.clear()
            self.__temp["name"] = ctx.ID().getText().encode()
            self.__temp["type"] = "procedure"
            self.__temp["list"] = []
            self.__sym_table.append(self.__temp.copy())
            self.__depth += 1;
            print "void",
            print "%s(" %self.__temp["name"],
            pass
        pass

    # Exit a parse tree produced by rp2cParser#subprogram_head.
    def exitSubprogram_head(self, ctx):
        if self.__sub_have_decl == 1:
            print '{'
        
        if ctx.getChildCount() == 6:
             self.__sym_table[-1]["return_type"] = self.__id_type               


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
                self.__temp.clear()
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
            self.__id_list.reverse()
            for i in self.__id_list:
                self.__temp.clear()
                self.__temp["name"] = i.encode()
                self.__temp["type"] = self.__id_type
                self.__temp["option"] = "VAR"
                self.table_insert(self.__temp)
            for i in self.__id_list:
                if self.__start_sub == 0:
                    self.__start_sub = 1;
                    print self.__temp["type"], "*%s" %i,
                else:
                    print ',%s' %self.__temp["type"], "*%s" %i,
            pass
        pass


    # Enter a parse tree produced by rp2cParser#compound_statement.
    def enterCompound_statement(self, ctx):
        if self.__sub_have_decl == 0 :
            print '{'
        else:
            self.__sub_have_decl = 0;
        pass

    # Exit a parse tree produced by rp2cParser#compound_statement.
    def exitCompound_statement(self, ctx):
        print ';'
        print '}'
        #print self.__sym_table


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
        del self.__id_list[0:]
        if ctx.identifier_list():
            print "scanf(",
        elif ctx.write_list():
            self.__write_control_form = ""
            print "cout << ",
            

    # Exit a parse tree produced by rp2cParser#statement.
    def exitStatement(self, ctx):
        if ctx.assignop():
            pass
        if ctx.identifier_list():
            control_form = ""
            self.__id_list.reverse()
            for i in range(len(self.__id_list)):
                if self.search_sub_pra(self.__id_list[i].encode()):
                    sym = self.search_sub_pra(self.__id_list[i].encode());
                elif self.search_main_pra(self.__id_list[i].encode()):
                    sym = self.search_main_pra(self.__id_list[i].encode());
                else:
                    print >>sys.stderr, "错误:欲读入的变量%s尚未定义" %self.__id_list[i].encode()
                    print ')'
                    return 
                if sym["type"] == 'int':
                    control_form += "%d ";
                elif sym["type"] == "double":
                    control_form += "%lf ";
            print ' "%s", ' %control_form,
            for i in range(len(self.__id_list)):
                if i!= 0 : print ',',
                print "&%s" %self.__id_list[i],
            print ")",
        elif ctx.write_list():
        #print ';'
            pass


    # Enter a parse tree produced by rp2cParser#variable.
    def enterVariable(self, ctx):
        if ctx.getChildCount()>0:
            sym = {}
            if self.search_sub_pra(ctx.ID().getText().encode()):
                sym = self.search_sub_pra(ctx.ID().getText().encode())
            elif self.search_main_pra(ctx.ID().getText().encode()):
                sym = self.search_main_pra(ctx.ID().getText().encode())
            else:
                print >>sys.stderr
                print >>sys.stderr, "错误:使用未声明的变量:%s" %ctx.ID().getText().encode()
            if "option" in sym:
                if sym["option"] == "VAR":
                    print "*%s" %ctx.ID().getText().encode(),
            else:
                print ctx.ID(),
                
            if ctx.getChildCount() == 4:
                print '[',
                if sym:
                    if "range_high" in sym:
                        pass
                    else:
                        print >>sys.stderr
                        print >>sys.stderr, "错误:变量%s不是一个数组类型" %ctx.ID().getText().encode()
                        print '[',
            if sym :
                self.__varable_type = sym["type"]
        pass

    # Exit a parse tree produced by rp2cParser#variable.
    def exitVariable(self, ctx):
        if ctx.getChildCount() == 4:
                print ']',
        pass


    # Enter a parse tree produced by rp2cParser#procedure_call_statement.
    def enterProcedure_call_statement(self, ctx):
        if ctx.ID:
            print "%s(" %ctx.ID().getText(),
        pass

    # Exit a parse tree produced by rp2cParser#procedure_call_statement.
    def exitProcedure_call_statement(self, ctx):
        print ")",
        pass


    # Enter a parse tree produced by rp2cParser#expr_list.
    def enterExpr_list(self, ctx):
        pass

    # Exit a parse tree produced by rp2cParser#expr_list.
    def exitExpr_list(self, ctx):
        if self.__expression_type == "int":
            self.__write_control_form += "%d "
        elif self.__expression_type == "double":
            self.__write_control_form += "%lf"
        pass


    # Enter a parse tree produced by rp2cParser#expression.
    def enterExpression(self, ctx):
        pass

    # Exit a parse tree produced by rp2cParser#expression.
    def exitExpression(self, ctx):
        if ctx.getChildCount() == 1:
            self.__expression_type = self.__simple_expr_type;
        elif ctx.getChildCount() == 3:
            self.__expression_type == "int"
            

    # Enter a parse tree produced by rp2cParser#simple_expr.
    def enterSimple_expr(self, ctx):
        pass

    # Exit a parse tree produced by rp2cParser#simple_expr.
    def exitSimple_expr(self, ctx):
        if ctx.getChildCount() == 1:
            self.__simple_expr_type = self.__term_type;
        elif ctx.getChildCount() == 3:
            if ctx.addop().getText() == 'OR':
                if self.__simple_expr_type != "int" or self.__term_type != "int":
                    print >>sys.stderr
                    print >>sys.stderr, "错误:OR的两侧应该是integer类型或是Boolean类型，而不是%s和%s类型" %(self.__simple_expr_type, self.__term_type)
            else:
                if self.__simple_expr_type == "double" or self.__term_type == "double":
                    self.__simple_expr_type = "double"
                else:
                    self.__simple_expr_type = "int"


    # Enter a parse tree produced by rp2cParser#term.
    def enterTerm(self, ctx):
        pass

    # Exit a parse tree produced by rp2cParser#term.
    def exitTerm(self, ctx):
        if ctx.getChildCount() == 1:
            self.__term_type = self.__factor_type;
        elif ctx.getChildCount() == 3:
            if ctx.mulop().getText() == '/':
                self.__term_type = "double"
            elif ctx.mulop().getText() == '*':
                if self.__term_type == "double" or self.__factor_type == "double":
                    self.__term_type = "double"
                else:
                    self.__term_type = "int"
            else:
                if self.__term_type != "int" or self.__factor_type != "int":
                    print >>sys.stderr
                    print >>sys.stderr, "错误:DIV/MOD/AND的两侧应该是integer类型或是Boolean类型，而不是%s和%s类型" %(self.__term_type, self.__factor_type)
                self.__term_type = self.__term_type;
        pass


    # Enter a parse tree produced by rp2cParser#factor.
    def enterFactor(self, ctx):
        sym = {}
        if ctx.ID():
            if self.search_sub_pra(ctx.ID().getText().encode()):
                sym = self.search_sub_pra(ctx.ID().getText().encode())
            elif self.search_main_pra(ctx.ID().getText().encode()):
                sym = self.search_main_pra(ctx.ID().getText().encode())
            else:
                print >>sys.stderr
                print >>sys.stderr, "错误:使用未声明的变量:%s" %ctx.ID().getText().encode()
                
            if ctx.getChildCount() ==1:
                if "option" in sym:
                    if sym["option"] == "VAR":
                        print "*%s" %ctx.ID().getText().encode(),
                        self.__factor_type = sym["type"]
                else :
                    print ctx.ID(),
                    if sym:
                        self.__factor_type = sym["type"]
                    
            if ctx.getChildCount() ==4:
                if ctx.expr_list():
                    print '%s(' %ctx.ID().getText().encode(),
                        
                elif ctx.expression():
                    print '%s[' %ctx.ID().getText().encode(),
        elif ctx.NUM():
            print ctx.NUM().getText(),
            self.__factor_type = "double"
        elif ctx.DIGITS():
            print ctx.DIGITS().getText(),
            self.__factor_type = "int"
        elif ctx.getChildCount() == 3 and ctx.expression():
            print '(',
        elif ctx.getChildCount() == 2 and ctx.factor():
            print '!',

        elif ctx.getChildCount() == 1 and ctx.getText() == "true":
            print 1,
            self.__factor_type = "int"
        elif  ctx.getChildCount() == 1 and ctx.getText() == "false":
            print 0,
            self.__factor_type = "int"
            
        pass

    # Exit a parse tree produced by rp2cParser#factor.
    def exitFactor(self, ctx):
        sym = {}
        if ctx.ID():
            if self.search_sub_pra(ctx.ID().getText().encode()):
                sym = self.search_sub_pra(ctx.ID().getText().encode())
            elif self.search_main_pra(ctx.ID().getText().encode()):
                sym = self.search_main_pra(ctx.ID().getText().encode())

                
            if ctx.getChildCount() ==4:
                if ctx.expr_list():
                    print')',
                    
                    if self.search_main_pra(ctx.ID().getText().encode()):
                        sym = self.search_main_pra(ctx.ID().getText().encode())
                    if "type" in sym:
                        if sym["type"] != "function":
                            print >>sys.stderr
                            print >>sys.stderr, "变量%s不是一个函数" %ctx.ID().getText().encode()
                            self.__factor_type = ""
                            return
                        elif "return_type" in sym:
                            self.__factor_type = sym["return_type"]
                    
                elif ctx.expression():
                    print']',
                    if sym:
                        if "range_high" in sym:
                            self.__factor_type = sym["type"]
                        else:
                            print >>sys.stderr
                            print >>sys.stderr, "错误:变量%s不是一个数组类型" %ctx.ID().getText().encode()
        elif ctx.getChildCount() == 3 and ctx.expression():
            print ')',
        elif ctx.getChildCount() == 2 and ctx.factor():
            if self.__factor_type != "int":
                print >>sys.stderr
                print >>sys.stderr, "错误:跟在not后面的应该是integer类型或是Boolean类型，而不是%s类型" %self.__factor_type
            else:
                pass    
        pass

    # Enter a parse tree produced by rp2cParser#mulop.
    def enterMulop(self, ctx):
        if ctx.getText() == '*':
            print '*',
        elif ctx.getText() == u'DIV':
            print '/',
        elif ctx.getText() == u'MOD':
            print '%',
        elif ctx.getText() == u'AND':
            print '&&',
            
    # Exit a parse tree produced by rp2cParser#mulop.
    def exitMulop(self, ctx):
        pass


    # Enter a parse tree produced by rp2cParser#addop.
    def enterAddop(self, ctx):
        if ctx.getText() != 'OR':
            print ctx.getText(),
        else :
            print '||',

    # Exit a parse tree produced by rp2cParser#addop.
    def exitAddop(self, ctx):
        pass


    # Enter a parse tree produced by rp2cParser#relop.
    def enterRelop(self, ctx):
        if ctx.getText() == '=':
            print '==',
        elif ctx.getText() == '<>':
            print '!=',
        elif ctx.getText():
            print ctx.getText(),
        pass

    # Exit a parse tree produced by rp2cParser#relop.
    def exitRelop(self, ctx):
        pass

        # Enter a parse tree produced by rp2cParser#assignop.
    def enterAssignop(self, ctx):
        print '=',
        pass

    # Exit a parse tree produced by rp2cParser#assignop.
    def exitAssignop(self, ctx):
        pass


        # Enter a parse tree produced by rp2cParser#then.
    def enterThen(self, ctx):
        print ')',
        pass

    # Exit a parse tree produced by rp2cParser#then.
    def exitThen(self, ctx):
        pass


    # Enter a parse tree produced by rp2cParser#else_.
    def enterElse_(self, ctx):
        print ';else',
        pass

    # Exit a parse tree produced by rp2cParser#else_.
    def exitElse_(self, ctx):
        pass


    # Enter a parse tree produced by rp2cParser#do.
    def enterDo(self, ctx):
        print ')',
        pass

    # Exit a parse tree produced by rp2cParser#do.
    def exitDo(self, ctx):
        pass


       # Enter a parse tree produced by rp2cParser#douhao.
    def enterDouhao(self, ctx):
        print ',',

    # Exit a parse tree produced by rp2cParser#douhao.
    def exitDouhao(self, ctx):
        pass

    # Enter a parse tree produced by rp2cParser#if_.
    def enterIf_(self, ctx):
        print "if(", 
        pass

    # Exit a parse tree produced by rp2cParser#if_.
    def exitIf_(self, ctx):
        pass


    # Enter a parse tree produced by rp2cParser#while_.
    def enterWhile_(self, ctx):
        print 'while(',
        pass

    # Exit a parse tree produced by rp2cParser#while_.
    def exitWhile_(self, ctx):
        pass
    
    # Enter a parse tree produced by rp2cParser#fenhao.
    def enterFenhao(self, ctx):
        print ';'

    # Exit a parse tree produced by rp2cParser#fenhao.
    def exitFenhao(self, ctx):
        pass
    
    # Enter a parse tree produced by rp2cParser#main_start.
    def enterMain_start(self, ctx):
        print "int main()"

    # Exit a parse tree produced by rp2cParser#main_start.
    def exitMain_start(self, ctx):
        pass

    
    # Enter a parse tree produced by rp2cParser#write_list.
    def enterWrite_list(self, ctx):
        pass
    
    # Exit a parse tree produced by rp2cParser#write_list.
    def exitWrite_list(self, ctx):
        pass


    # Enter a parse tree produced by rp2cParser#douhao_.
    def enterDouhao_(self, ctx):
        pass

    # Exit a parse tree produced by rp2cParser#douhao_.
    def exitDouhao_(self, ctx):
        print "<<",
        pass



