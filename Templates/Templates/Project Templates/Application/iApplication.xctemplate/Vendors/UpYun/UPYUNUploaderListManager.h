//
//  UPYUNUploaderListManager.h
//  YooSayMyPose
//
//  Created by zeng hui on 14/12/30.
//  Copyright (c) 2014年 zeng. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface UPYUNUploaderListManager : NSObject {
    
}

// 管理列表
@property(nonatomic, strong) NSMutableArray *lists;

- (void)addTask:(id)file;

@end
