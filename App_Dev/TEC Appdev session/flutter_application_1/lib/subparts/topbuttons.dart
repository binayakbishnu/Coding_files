import 'package:flutter/material.dart';

class TopButtons extends StatelessWidget {
  const TopButtons({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceAround,
      children: [
        Container(
          color: Colors.orange,
          child: Padding(
            padding: const EdgeInsets.all(8.0),
            child: Text('All rooms'),
          ),
        ),
        Container(
          color: Colors.orange,
          child: Padding(
            padding: const EdgeInsets.all(8.0),
            child: Text('All rooms'),
          ),
        ),
        Container(
          color: Colors.orange,
          child: Padding(
            padding: const EdgeInsets.all(8.0),
            child: Text('All rooms'),
          ),
        ),
        Container(
          color: Colors.orange,
          child: Padding(
            padding: const EdgeInsets.all(8.0),
            child: Text('All rooms'),
          ),
        ),
      ],
    );
  }
}
