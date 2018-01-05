#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Gwent_Calculate 昆特牌多功能决斗计算器
# Author:hongfeiyu

import sys

def attack(a,b):
	#a打b,[0]为战力,[1]为护甲
	b[1]=b[1]-a[0]
	if b[1]<0:
		b[0]=b[0]+b[1]
		b[1]=0
	if b[0]<0:
		b[0]=0
	return a,b

def mode0(a):
	enemy=[[0]*2]
	max_damage=0
	damage=0
	enemy=a.split(" ")
	for i in range(len(enemy)):
		if not ',' in enemy[i]:
			enemy[i]=enemy[i]+',0'
		enemy[i]=enemy[i].split(',')
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

	print u"最大收益：用",A,u"攻击",B,u"得到最大收益：",max_damage
	while B[0]>0 and A[0]>0:
		print B,A,'->',
		A,B=attack(A,B)
		B,A=attack(B,A)
	print B[0],A[0]

def mode1(a):
	enemy=[[0]*2]
	max_damage=0
	damage=0
	enemy=a.split(" ")
	for i in range(len(enemy)):
		if not ',' in enemy[i]:
			enemy[i]=enemy[i]+',0'
		enemy[i]=enemy[i].split(',')
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
		print enemy[i][0],enemy[j][0],a[0],b[0]
		print damage
		if damage>max_damage:
			max_damage=damage
			A=enemy[i]
			B=enemy[j]

	print u"最大收益：用",A,u"攻击",B,u"得到最大收益：",max_damage
	while B[0]>0 and A[0]>0:
		print B,A,'->',
		A,B=attack(A,B)
		B,A=attack(B,A)
	print B[0],A[0]


print u"\nGwent_Calculate 昆特牌多功能决斗计算器 1.0\n"
print u"\n输入x在两个模式之间切换，输入q退出"
print u"\n如果需要计算护甲，在战力后面加上逗号和护甲值，注意要用英文逗号例如12,2"
print u"\n不同战力之间用空格隔开，但只能用一个空格，不要加多余的空格，例如12,2 1 3 4"
mode=0

while 1:
	if mode==0:
		a=raw_input("\n伊欧菲斯：冥想 计算模式\n输入敌方场上所有单位目前战力值(以空格隔开)\n>>>")
	else:
		a=raw_input("\n普通决斗 计算模式\n输入己方决斗发起者战力值(作为第一个)和敌方场上单位战力值(以空格隔开)\n>>>")
	if 'q' in a:
		break
	elif 'x' in a:
		mode=1^mode
		a=raw_input("\n普通决斗 计算模式\n输入己方决斗发起者战力值(作为第一个)和敌方场上单位战力值(以空格隔开)\n>>>")
	if mode==0:
		mode0(a)
	else:
		mode1(a)
