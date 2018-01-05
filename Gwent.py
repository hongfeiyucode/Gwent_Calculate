#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Gwent_Calculate 昆特牌多功能决斗计算器
# Author:hongfeiyu

import sys


def mode0(a):
	enemy=[]
	max_damage=0
	damage=0
	A=0
	B=0
	enemy=a.split(" ")
	enemy=map(int,enemy)
	for i in range(len(enemy)):
		for j in range(len(enemy)):
			if i==j:
				continue
			i=enemy[i]
			j=enemy[j]
			big=i if i>j else j
			small=j if i>j else i
			while big>0 and small>0:
				big=big-small if big>=small else 0
				small=small-big if small>=big else 0
			damage=i+j-big-small
			if damage>max_damage:
				max_damage=damage
				A=j if i>j else i
				B=i if i>j else j

	print u"最大收益：用",A,u"攻击",B,u"得到最大收益：",max_damage,u"\n战力变化为："
	while B>0 and A>0:
		print B,A,'->',
		B=B-A if B>=A else 0
		A=A-B if A>=B else 0
	print B,A

def mode1(a):
	enemy=[]
	max_damage=0
	damage=0
	A=0
	B=0
	enemy=a.split(" ")
	enemy=map(int,enemy)
	i=enemy[0]
	enemy=enemy[1:]
	for j in enemy:
		big=j
		small=i
		while big>0 and small>0:
			big=big-small if big>=small else 0
			small=small-big if small>=big else 0
		damage=j-big-(i-small)
		if damage>max_damage:
			max_damage=damage
			A=i
			B=j

	print u"最大收益：用",A,u"攻击",B,u"得到最大收益：",max_damage
	while B>0 and A>0:
		print B,A,'->',
		B=B-A if B>=A else 0
		A=A-B if A>=B else 0
	print B,A


print u"\nGwent_Calculate 昆特牌多功能决斗计算器 1.0\n"
print u"\n输入x在两个模式之间切换，输入q退出\n"
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
