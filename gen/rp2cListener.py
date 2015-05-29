# -*- coding: cp936 -*-
# Generated from java-escape by ANTLR 4.5
from antlr4 import *
import copy
import sys

# This class defines a complete listener for a parse tree produced by rp2cParser.
class rp2cListener(ParseTreeListener):
    def __init__(self):
        self.__id_list = []  ##记录identifier_list中遍历过的ID
        self.__id_type = ""  ##记录访问type时的ID类型
        self.__id_range_low = 0 ##记录数据类型的下界
        self.__id_range_high = 0 
        self.__sym_table = []   ##符号表
        self.__sym_table_temp = []  ##临时符号表
        self.__temp = {}    ##用于插入符号表前的临时dict
        self.__depth = 0;   ##进入符号表的深度
        self.__start_sub = 0; ##记录子函数是否已经开始
        self.__expression = ""  ##似乎没有用到?
        self.__simple_expr = "" ##似乎没有用到?
        self.__term = ""
        self.__factor = ""
        self.__sub_have_decl = 0 ##记录子函数是否有变量定义，主要用于判断子函数中{符号的位置
        self.__variable_type = "" #记录variable的类型
        self.__expression_type = "" #记录expression的类型
        self.__simple_expr_type = ""
        self.__term_type = ""
        self.__factor_type = ""
        self.__have_error = 0 #没有用到
        self.__write_control_form = "" #没有用到
        self.__if_write = 0
	self.__expr_list_num = 0
        self.__parameter_lists_num = 0

    def del_sub_pra(self): #用于在退出函数后将变量list清空
        if "list" in self.__sym_table[-1]:
            if self.__sym_table[-1]["list"]:
                del self.__sym_table[-1]["list"][0:] 

    def search_sub_pra(self, ID): #用于在当前的函数中查找变量定义
        if "list" in self.__sym_table[-1]:
            for i in self.__sym_table[-1]["list"]:
                if i["name"] == ID:
                    return i
        return None

    def search_main_pra(self, ID): #用于在主函数查找变量定义
        for i in self.__sym_table:
            if i["name"] == ID:
                return i
        return None

    def check_repetition(self, ID): #用于查找变量是否重复定义
        temp = self.__sym_table;
        for i in range(self.__depth):
            temp = temp[-1]["list"];
            #print temp
        for i in temp:
            if i["name"] == ID : return False;
        return True
        pass

    def table_insert(self, sym): #用于将变量根据深度depth插入符号表中
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
        if "ID" in dir(ctx):   #如果ID存在，将其插入__id_list中
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
        del self.__id_list[0:] #清空__id_list
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
                for i in range(len(self.__id_list)): #存入符号表
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
                
                print "struct", #翻译部分
                print self.__id_list[0],
                for i in self.__id_list[1:]:
                    print ',' , i,
                print "{"
            
        elif ctx.getChildCount() == 7: #array_type
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
            print "}" ##有雷
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
        self.del_sub_pra() #清空当前子函数的符号表
        self.__sub_have_decl = 0
        self.__depth -= 1; #深度depth减1

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
            
            if ctx.standard_type().getText() == "integer": #翻译部分
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
        self.__sym_table[-1]["pra_num"] = self.__parameter_lists_num
        if self.__sub_have_decl == 1:
            print '{'
        
        if ctx.getChildCount() == 6: #funciton:
            self.__sym_table[-1]["return_type"] = self.__id_type
            print "%s __%s;" %(self.__id_type, self.__sym_table[-1]["name"]) #用于解决c/c++语言与pascal语言函数返回值不同，用__function_name来记录返回值
                              
    # Enter a parse tree produced by rp2cParser#arguments.
    def enterArguments(self, ctx):
        self.__parameter_lists_num = 0
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
        if ctx.getChildCount() == 3: #定义时没有VAR
            self.__id_list.reverse()
            for i in self.__id_list:
                self.__temp.clear()
                self.__temp["name"] = i.encode()
                self.__temp["type"] = self.__id_type
                self.table_insert(self.__temp)
            for i in self.__id_list:
                self.__parameter_lists_num += 1;
                if self.__start_sub == 0:
                    self.__start_sub = 1;
                    print self.__temp["type"], i,
                else:
                    print ',%s' %self.__temp["type"], i,
            pass
        elif ctx.getChildCount() == 4: #定义时有VAR,dict多一个属性option，其中的值赋为VAR
            self.__id_list.reverse()
            for i in self.__id_list:
                self.__parameter_lists_num += 1;
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
        if self.__sym_table[-1]["type"] == "function" and self.__sym_table[-1]["list"]: #同样用于解决函数返回值的问题
            print "return __%s;" %self.__sym_table[-1]["name"]
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
            if self.__variable_type != self.__expression_type:
                print >>sys.stderr
                print >>sys.stderr,"错误：赋值号两侧类型不同,左侧为%s类型，右侧为%s类型" %(self.__variable_type, self.__expression_type)
        if ctx.identifier_list(): #read语句
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
                    control_form += "%d";
                elif sym["type"] == "double":
                    control_form += "%lf";
            print ' "%s", ' %control_form,
            for i in range(len(self.__id_list)):
                if i!= 0 : print ',',
                print "&%s" %self.__id_list[i],
            print ")",
        elif ctx.write_list(): #write语句
            print " << ' '",
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
            if "option" in sym: #用于处理形式参数和实际参数的区别
                if sym["option"] == "VAR":
                    print "*%s" %ctx.ID().getText().encode(),
					
		    self.__variable_type = sym["type"]
            elif "type" in sym and sym["type"] == "function":          #用于出来函数返回用法不同的问题
                print "__%s" %ctx.ID(),
		self.__variable_type = sym["return_type"]
            else:
                print ctx.ID(),
		self.__variable_type = sym["type"]
                
            if ctx.getChildCount() == 4:
                print '[',
                if sym:
                    if "range_high" in sym:
                        pass
                    else:
                        print >>sys.stderr
                        print >>sys.stderr, "错误:变量%s不是一个数组类型" %ctx.ID().getText().encode()
        pass

    # Exit a parse tree produced by rp2cParser#variable.
    def exitVariable(self, ctx):
        if ctx.getChildCount() == 4:
            print ']',
            if self.__expression_type != "int":
                print >>sys.stderr
                print >>sys.stderr, ("错误:数组下标应该是int类型，而不是%s类型") %self.__expression_type
        pass


    # Enter a parse tree produced by rp2cParser#procedure_call_statement.
    def enterProcedure_call_statement(self, ctx):
        
        self.__expr_list_num = 0
        if ctx.ID:
            print "%s(" %ctx.ID().getText(),
        pass

    # Exit a parse tree produced by rp2cParser#procedure_call_statement.
    def exitProcedure_call_statement(self, ctx):
        print ")",
        sym = {}
        if ctx.ID:
            for i in self.__sym_table:
                if i["name"] == ctx.ID().getText().encode():
                    sym = i
            if "type" in sym:
                if sym["type"] != "procedure":
                    print >>sys.stderr
                    print >>sys.stderr, "错误: %s不是一个过程，而是一个%s类型" %(ctx.ID().getText().encode(), sym["type"])
                elif self.__expr_list_num +1 != sym["pra_num"]:
                    print >>sys.stderr
                    print >>sys.stderr, "错误：调用过程%s时输入的参数个数不正确，应该输入%d个，输入了%d个" %(ctx.ID().getText().encode(), sym["pra_num"], self.__expr_list_num +1)
            else:                                   
                print >>sys.stderr
                print >> sys.stderr, "错误: 过程%s不存在" %ctx.ID().getText().encode()
                
        pass


    # Enter a parse tree produced by rp2cParser#expr_list.
    def enterExpr_list(self, ctx):
        pass

    # Exit a parse tree produced by rp2cParser#expr_list.
    def exitExpr_list(self, ctx):
        if self.__expression_type == "int":
            self.__write_control_form += "%d "
        elif self.__expression_type == "double":
            self.__write_control_form += "%lf "
        pass


    # Enter a parse tree produced by rp2cParser#expression.
    def enterExpression(self, ctx):
        pass

    # Exit a parse tree produced by rp2cParser#expression.
    def exitExpression(self, ctx):
        if ctx.getChildCount() == 1:
            self.__expression_type = self.__simple_expr_type;
        elif ctx.getChildCount() == 3:
            self.__expression_type = "int"
            

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
                    self.__expr_list_num = 0
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
                            print >>sys.stderr, "错误：变量%s不是一个函数" %ctx.ID().getText().encode()
                            self.__factor_type = ""
                            return
                        elif "return_type" in sym:
                            self.__factor_type = sym["return_type"]
                            
                    if ("pra_num" in sym) and (self.__expr_list_num +1 != sym["pra_num"]):
                        print >>sys.stderr
                        print >>sys.stderr, "错误：调用函数%s时输入的参数个数不正确，应该输入%d个，输入了%d个" %(sym["name"], sym["pra_num"], self.__expr_list_num +1)
                        
                elif ctx.expression():
                    print']',
                    if sym:
                        if "range_high" in sym:
                            self.__factor_type = sym["type"]
                        else:
                            print >>sys.stderr
                            print >>sys.stderr, "错误:变量%s不是一个数组类型" %ctx.ID().getText().encode()
                    if self.__expression_type != "int":
                        print >>sys.stderr
                        print >>sys.stderr, ("错误:数组下标应该是int类型，而不是%s类型") %self.__expression_type
                        
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
        if self.__expression_type != "int":
            print >>sys.stderr
            print >>sys.stderr, "错误:if语句后的表达式应为Boolean类型，而不应是%s类型" %self.__expression_type
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

        if self.__expression_type != "int":
            print >>sys.stderr
            print >>sys.stderr, "错误:while语句后的表达式应为Boolean类型，而不应是%s类型" %self.__expression_type
        pass

    # Exit a parse tree produced by rp2cParser#do.
    def exitDo(self, ctx):
        pass


       # Enter a parse tree produced by rp2cParser#douhao.
    def enterDouhao(self, ctx):
        self.__expr_list_num += 1
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
        print "<< ' ' << ",
        pass



