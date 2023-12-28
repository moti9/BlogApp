import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Login from './auth/Login';
import Footer from './components/Footer';
import Home from './pages/Home';
import BlogHome from './blog/BlogHome';
import { AuthProvider } from './auth/AuthContext';
import Signup from './auth/Signup';
import About from './pages/About';
import BlogPost from './blog/BlogPost';
import WriteBlog from './blog/WriteBlog';
import BlogEdit from './blog/BlogEdit';
import ProfileHome from './user/ProfileHome';


function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Navbar />
        <Routes>
          <Route path='/'>
            <Route index element={<Home />} />

          </Route>
          <Route path='/about' element={<About />} />
          <Route path='/user'>
            <Route index element={<ProfileHome />} />
            <Route path="login" element={<Login />} />
            <Route path="signup" element={<Signup />} />
          </Route>
          <Route path="/blog">
            <Route index element={<BlogHome />} />
            <Route path='newpost' element={<WriteBlog />} />
            <Route path='post/:id' element={<BlogPost />} />
            <Route path='post/:id/edit' element={<BlogEdit />} />
          </Route>
        </Routes>
        <Footer />
      </BrowserRouter>
    </AuthProvider>
  );
}

export default App;
