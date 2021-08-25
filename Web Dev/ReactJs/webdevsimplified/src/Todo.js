import React from 'react'

export default function Todo({ todo }) {
    return (
        <div>
            {/* {todo} */}

            {/* after making id name attrs */}
            {/* {todo.name} */}
            {/* making checkboxes to show completion */}
            <label>
                <input type="checkbox" checked={todo.complete}></input>
                {todo.name}
            </label>
        </div>
    )
}
