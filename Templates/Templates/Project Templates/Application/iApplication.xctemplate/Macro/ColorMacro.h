//
//  ColorMacro.h
//  CooLaDingNOTwo
//
//  Created by xy on 16/1/14.
//  Copyright © 2016年 coolading. All rights reserved.
//

#ifndef ColorMacro_h
#define ColorMacro_h


#pragma mark - color
/* *** DEBUG DEFINE *** */
// 测试用色（正常状态下置0，为透明色）
#if DEBUG
#define KTEST_COLOR  ([UIColor  colorWithRed:arc4random() % 10 / 10.0f \
green:arc4random() % 10 / 10.0f \
blue:arc4random() % 10 / 10.0f \
alpha:0.8] )
#else
#define KTEST_COLOR ([UIColor clearColor])
#endif



#define Kcolora(r, g, b, a) [UIColor colorWithRed:r / 255.0 green:g / 255.0 blue:b / 255.0 alpha:a]
#define Kcolor(r, g, b)     Kcolora(r, g, b, 1)


#define Kwhite              Kcolora(255, 255, 255, .8);
//#define Kwhite              Kcolora(255, 255, 255, .8);
#define KlightGrayColor         [UIColor lightGrayColor]

#define KYello              Kcolora(255, 255, 255, .8)

#define KRed                Kcolor(230, 5,   39      )
#define KWhitch             Kcolor(244, 244, 244     )
#define Kbackground         Kcolor(227, 227, 227.0   )
#define KbackgroundNight    Kcolor(167, 167, 167.0   )

#define KBlue               Kcolor(36,  75,  115     )

#define KbackgroundBlack    Kcolor(16, 16, 16 )
//#define KbackgroundBlack    Kcolor(0, 0, 0   )

#define KInsBlue            Kcolor(36, 75, 115)

//#define KToolBarColor       Kcolor(37, 50, 69)
//#define KToolBarSelectColor Kcolor(37, 50, 69)

#define KToolBarBlackSelectColor    Kcolor(18, 19, 20)
#define KToolBarBlackColor          Kcolor(37, 50, 69)//Kcolor(28, 28, 31)



#endif /* ColorMacro_h */
