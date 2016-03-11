import pygame

def vby1(self,u,a,t):
	"v=u+at"
	assert t>=0
	return (u+a*t)

def vby3(self,u,a,s):
	"v2=u2+2as"
	temp = u*u + 2*a*s
	return (math.sqrt(temp))
	
def uby1(self,v,a,t):
	"u=v-at"
	assert t>=0
	return (v-a*t)

def uby2(self,s,a,t):
	"u=(s-a*t*t/2)/t"
	assert t>0
	temp = s-a*t*t/2
	return (temp/t)

def uby3(self,v,a,s):
	"u2=v2-2as"
	temp= v*v - 2*a*s
	return (math.sqrt(temp))
	

	
