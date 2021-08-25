import React from 'react'
import Todo from './Todo'

export default function TodoList({ todos }) {
    // return (
    //     <div>
    //         {/* Hello World */}
    //         {todos.length}
    //     </div>
    // )

    return (
        //!mapping the Todo object from Todo.js
        todos.map(todo => {
            // return <Todo key={todo} todo={todo}/>
            // key has to be unique
            // extra key attribute make react only re-render those which change and not all the members
            return <Todo key={todo.id} todo={todo} />
        })
    )
}
