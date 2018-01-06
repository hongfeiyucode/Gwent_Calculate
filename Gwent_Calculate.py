#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Gwent_Calculate 昆特牌多功能决斗计算器
# Author:hongfeiyu
# https://github.com/hongfeiyucode/Gwent_Calculate

import sys

print u"\n>>>  Gwent_Calculate 昆特牌多功能决斗计算器 3.0  <<<\n"
print u"\n输入x加数字在 1伊欧菲斯：冥想 2赛尔奇克 3竞技场冠军 4店店 5冰巨魔冰霜之下 6自由决斗六种模式之间切换，输入q退出"
print u"\n如果需要计算护甲，在战力后面加上加号和护甲值，例如12+2"
print u"\n不同战力之间用空格隔开，但只能用一个空格，不要加多余的空格，例如12+2 1 3 4"

def attack(a,b):
	#a打b,[0]为战力,[1]为护甲
	b[1]=b[1]-a[0]
	if b[1]<0:
		b[0]=b[0]+b[1]
		b[1]=0
	if b[0]<0:
		b[0]=0
	return a,b

def attack5(a,b):
	b[1]=b[1]-a[0]*2
	if b[1]<0:
		b[0]=b[0]+b[1]
		b[1]=0
	if b[0]<0:
		b[0]=0
	return a,b

def mode1(a):
	enemy=[[0]*2]
	max_damage=0
	damage=0
	enemy=a.split(" ")
	for i in range(len(enemy)):
		if not '+' in enemy[i]:
			enemy[i]=enemy[i]+'+0'
		enemy[i]=enemy[i].split('+')
		enemy[i]=map(int,enemy[i])
		#print enemy[i][0],enemy[i][1]
	A=B=[0,0]
	for i in range(len(enemy)):
		for j in range(len(enemy)):
			if i==j:
				continue
			a=enemy[i][:]
			b=enemy[j][:]
			while a[0]>0 and b[0]>0:
				a,b=attack(a,b)
				b,a=attack(b,a)
			damage=enemy[i][0]+enemy[j][0]-a[0]-b[0]
			if damage>max_damage:
				max_damage=damage
				A=enemy[i]
				B=enemy[j]

	print u"最大收益：用",A,u"攻击",B,u"得到最大收益：",max_damage,"\n战力变化过程:",
	while B[0]>0 and A[0]>0:
		print A,B,'->',
		A,B=attack(A,B)
		print A,B,'->',
		B,A=attack(B,A)
	print A,B

def mode2(a):
	enemy=[[0]*2]
	max_damage=0
	damage=0
	enemy=a.split(" ")
	for i in range(len(enemy)):
		if not '+' in enemy[i]:
			enemy[i]=enemy[i]+'+0'
		enemy[i]=enemy[i].split('+')
		enemy[i]=map(int,enemy[i])
		#print enemy[i][0],enemy[i][1]
	A=B=[0,0]
	i=0
	for j in range(1,len(enemy)):
		a=enemy[i][:]
		b=enemy[j][:]
		while a[0]>0 and b[0]>0:
			a,b=attack(a,b)
			b,a=attack(b,a)
		damage=enemy[i][0]+enemy[j][0]-a[0]-b[0]
		if damage>max_damage:
			max_damage=damage
			A=enemy[i]
			B=enemy[j]

	print u"最大收益：用",A,u"攻击",B,u"得到最大收益：",max_damage,"\n战力变化过程:",
	while B[0]>0 and A[0]>0:
		print A,B,'->',
		A,B=attack(A,B)
		print A,B,'->',
		B,A=attack(B,A)
	print A,B

def mode5(a):
	enemy=[[0]*2]
	max_damage=0
	damage=0
	enemy=a.split(" ")
	for i in range(len(enemy)):
		if not '+' in enemy[i]:
			enemy[i]=enemy[i]+'+0'
		enemy[i]=enemy[i].split('+')
		enemy[i]=map(int,enemy[i])
		#print enemy[i][0],enemy[i][1]
	A=B=[0,0]
	i=0
	for j in range(1,len(enemy)):
		a=enemy[i][:]
		b=enemy[j][:]
		while a[0]>0 and b[0]>0:
			a,b=attack5(a,b)
			b,a=attack(b,a)
		damage=enemy[i][0]+enemy[j][0]-a[0]-b[0]
		if damage>max_damage:
			max_damage=damage
			A=enemy[i]
			B=enemy[j]

	print u"最大收益：用",A,u"攻击",B,u"得到最大收益：",max_damage,"\n战力变化过程:",
	while B[0]>0 and A[0]>0:
		print A,B,'->',
		A,B=attack5(A,B)
		print A,B,'->',
		B,A=attack(B,A)
	print A,B

mode=1

while 1:
	if mode==1:
		print u"\n伊欧菲斯：冥想 计算模式\n输入敌方场上所有单位目前战力值(以空格隔开)\n>>>",
		a=raw_input()
	elif mode==2:
		print u"\n赛尔奇克 计算模式\n输入敌方场上所有单位目前战力值(以空格隔开)\n>>>",
		a=raw_input()
	elif mode==3:
		print u"\n竞技场冠军 计算模式\n输入敌方场上所有单位目前战力值(以空格隔开)\n>>>",
		a=raw_input()
	elif mode==4:
		print u"\n店店 计算模式\n输入敌方场上所有单位目前战力值(以空格隔开)\n>>>",
		a=raw_input()
	elif mode==5:
		print u"\n冰巨魔冰霜之下 计算模式\n输入敌方场上所有单位目前战力值(以空格隔开)\n>>>",
		a=raw_input()
	elif mode==6:
		print u"\n自由决斗 计算模式\n输入决斗发起者作为第一个数值和敌方战力值(以空格隔开)\n>>>",
		a=raw_input()
	if 'q' in a:
		break
	elif 'x' in a:
		if '1' in a:
			mode=1
		elif '2' in a:
			mode=2
		elif '3' in a:
			mode=3
		elif '4' in a:
			mode=4
		elif '5' in a:
			mode=5
		elif '6' in a:
			mode=6
		print u"计算模式已切换！"
		continue
	if mode==1:
		mode1(a)
	elif mode==2:
		mode2("7+3 "+a)
	elif mode==3:
		mode2("7 "+a)
	elif mode==4:
		mode2("12 "+a)
	elif mode==5:
		mode5("4 "+a)
	elif mode==6:
		mode2(a)