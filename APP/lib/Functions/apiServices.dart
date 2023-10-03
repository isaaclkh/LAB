// HAVING AN ERROR = NOT CONNECTED

import 'dart:convert';
import 'package:flutter/cupertino.dart';
import 'package:http/http.dart' as http;
import 'package:pibo/components/openai_key.dart';

class Api{
  static final Uri url = Uri.parse("https://api.openai.com/v1/images/generations");

  static final headers = {
    "Content-Type" : "application/json",
    "Authorization" : "Bearer $apiKey",
  };

  static generateImage(String text) async{
    http.Response res = await http.post(
      url,
      headers: headers,
      body: jsonEncode({"prompt" : text, "n" : 1, "size": "1024x1024",}),
    );

    if(res.statusCode == 200){
      print('connected!');
      var data = jsonDecode(res.body.toString());
      return data['data'][0]['url'].toString();
    }
    else{
      debugPrint('Failed to get a forecast with status code, ${res.statusCode}');
      print("Failed to get image");
    }
  }

  Future<String> getChatGPTResponse(String userInput) async {
    final response = await http.post(
      Uri.parse('http://your-backend-server.com/api/chatgpt'),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
      },
      body: jsonEncode(<String, String>{
        'user_input': userInput,
      }),
    );

    if (response.statusCode == 200) {
      return response.body;
    } else {
      throw Exception('Failed to load ChatGPT response');
    }
  }
}