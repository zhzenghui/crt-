//
//  DTOAuthFunctions.h
//  OAuthTest
//
//  Created by Oliver Drobnik on 6/23/14.
//  Copyright (c) 2014 Cocoanetics. All rights reserved.
//
#import <Foundation/Foundation.h>

// splits query string and returns dictionary
NSDictionary *DTOAuthDictionaryFromQueryString(NSString *string);