__author__ = 'Sawl_Stone'

class Symbol:
    def __init__(self, s_name, s_type):
        self.s_name = s_name
        self.s_type = s_type


class Word(Symbol):
    def __init__(self, w_name):
        self.w_name = w_name


    def small_big(self):
        small_list = [q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l,z,x,c,v,b,n,m]
        big_list = [Q,W,E,R,T,Y,U,I,O,P,A,S,D,F,G,H,J,K,L,Z,X,C,V,B,N,M]
        self.small = i in range(small_list)
        self.big = i in range(big_list)
        print(self.big)


class Sentence:
    pass


cupakabra = Word("cupakabra", "q", "Q")
cupakabra.small_big()