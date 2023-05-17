
import 'package:flutter/services.dart';

class ParsingComment{
  parse(String comment){
    String temp1, temp2, temp3, temp4;
    temp1 = comment.replaceAll("\"", '');
    temp2 = temp1.replaceAll("이야", '');
    temp3 = temp2.replaceAll(".", '');
    temp4 = temp3.replaceAll("말씀", '');
    return temp4;
  }

  extractSpecial(String comment){
    String temp;
    // String regex = r'[^\p{Alphabetic}\p{Mark}\p{Decimal_Number}\p{Connector_Punctuation}\p{Join_Control}\s]+';
    // temp = comment.replaceAll(RegExp(regex, unicode: true), '');
    temp = comment.replaceAll("\"", '');
    return temp;
  }
}