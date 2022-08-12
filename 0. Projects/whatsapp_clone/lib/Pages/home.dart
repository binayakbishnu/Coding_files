import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:whatsapp_clone/Pages/newchatgroup.dart';
import 'package:whatsapp_clone/homesections/chat.dart';

class Home extends StatelessWidget {
  final String title='Whatsapp';

  const Home({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: <Widget>[
            Text(title),
            Row(
              children: const <Widget>[
                Icon(Icons.search),
                SizedBox(
                  width: 10,
                ),
                Icon(Icons.more_vert),
              ],
            ),
          ],
        ),
      ),
      body: Center(
        child: Container(
          color: Theme.of(context).colorScheme.background,
          child: Padding(
            padding:
            const EdgeInsets.symmetric(vertical: 10.0, horizontal: 15.0),
            child: SingleChildScrollView(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.start,
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: const <Widget>[
                  Chat(),
                  SizedBox(height: 8,),
                  Chat(),
                  SizedBox(height: 8,),
                  Chat(),
                  SizedBox(height: 8,),
                  Chat(),
                  SizedBox(height: 8,),
                  Chat(),
                  SizedBox(height: 8,),
                  Chat(),
                  SizedBox(height: 8,),
                  Chat(),
                  SizedBox(height: 8,),
                  Chat(),
                  SizedBox(height: 8,),
                  Chat(),
                  SizedBox(height: 8,),
                  Chat(),
                  SizedBox(height: 8,),
                  Chat(),
                  SizedBox(height: 8,),
                  Chat(),
                  SizedBox(height: 8,),
                  Chat(),
                  SizedBox(height: 8,),
                  Chat(),
                  SizedBox(height: 8,),
                  Chat(),
                ],
              ),
            ),
          ),
        ),
      ),
      floatingActionButton: FloatingActionButton(
        backgroundColor: Theme.of(context).colorScheme.primary,
        foregroundColor: Theme.of(context).colorScheme.onPrimary,
        splashColor: Theme.of(context).splashColor,
        focusColor: Theme.of(context).focusColor,
        onPressed: () {
          if (kDebugMode) {
            print("New chat/group");
          }
          Navigator.push(
            context,
            MaterialPageRoute(builder: (context) => const NewChatGroup()),
          );
        },
        tooltip: 'New chat/group',
        child: const Icon(Icons.chat),
      ),
    );
  }
}
