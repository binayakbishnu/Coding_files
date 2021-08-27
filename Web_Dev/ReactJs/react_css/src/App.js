import Inline_Style from "./Inline_Style";
import Stylesheet from "./Stylesheet";

function App() {
  return (
    <div className="App">
      <Stylesheet font_color={true} font_size={true} />
      <Inline_Style />
    </div>
  );
}

export default App;
