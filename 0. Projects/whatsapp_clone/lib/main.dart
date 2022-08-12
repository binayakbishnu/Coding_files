import 'package:flutter/material.dart';
import 'package:whatsapp_clone/Pages/home.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Whatsapp',
      theme: ThemeData(
        appBarTheme: const AppBarTheme(
            backgroundColor: Color.fromRGBO(72, 72, 72, 1.0),
            foregroundColor: Colors.white),
        colorScheme: const ColorScheme(
          brightness: Brightness.dark,
          primary: Color.fromRGBO(35, 200, 97, 1.0),
          onPrimary: Colors.white,
          secondary: Colors.blue,
          onSecondary: Colors.white,
          error: Colors.red,
          onError: Colors.black,
          background: Colors.black54,
          onBackground: Colors.grey,
          surface: Colors.white,
          onSurface: Colors.black,
        ),
        splashColor: const Color.fromRGBO(97, 97, 97, 0.8),
        focusColor: Colors.grey[500],
      ),
      home: const Home(),
    );
  }
}
