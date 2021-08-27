import React from 'react'
import './mystyles.css'

function Stylesheet(props) {
    let font_color = props.font_color ? 'primary' : ''
    let font_size = props.font_size ? 'font-xl' : ''
    return (
        <div>
            {/* <h1 className={className}>Stylesheets</h1> */}
            {/* <h1 className={`${font_color} font-xl`}>Stylesheets</h1> */}
            <h1 className={`${font_color} ${font_size}`}>Stylesheets</h1>
        </div>
    )
}

export default Stylesheet
