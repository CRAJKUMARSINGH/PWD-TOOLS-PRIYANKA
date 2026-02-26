import streamlit as st
from utils.branding import apply_custom_css, show_header
from utils.navigation import create_breadcrumb, create_back_button

# Page configuration
st.set_page_config(
    page_title="Tender Processing | PWD Tools Hub",
    page_icon="📑",
    layout="wide"
)

# Apply branding
apply_custom_css()
create_breadcrumb("Tender Processing")

def main():
    # Center content with full width
    col1, col2, col3 = st.columns([1, 8, 1])
    with col2:
        # Three access buttons
        st.markdown("### Choose Access Method:")
        st.warning("⚠️ This tool requires login authentication")
        
        col_a, col_b, col_c = st.columns(3)
        
        with col_a:
            if st.button("🔗 Open in New Tab", use_container_width=True):
                st.markdown(
                """
                <script>
                    window.open('https://priyankatenderfinal-unlhs2yudbpg2ipxgdggws.streamlit.app/', '_blank');
                    (function(){
                      if(!document.getElementById('balloon-styles')){const css=`.balloons-container{position:fixed;inset:0;pointer-events:none;overflow:hidden;z-index:9999}.balloon{position:absolute;bottom:-10%;width:22px;height:28px;border-radius:50% 50% 45% 45%;opacity:.9;animation:floatUp linear forwards}.balloon:after{content:'';position:absolute;bottom:-8px;left:50%;transform:translateX(-50%);width:2px;height:10px;background:rgba(0,0,0,.2)}@keyframes floatUp{to{transform:translateY(-120vh)}}`;const s=document.createElement('style');s.id='balloon-styles';s.textContent=css;document.head.appendChild(s);} 
                      if(!document.getElementById('confetti-styles')){const css2=`.confetti-container{position:fixed;inset:0;pointer-events:none;overflow:hidden;z-index:9999}.confetti{position:absolute;top:-10%;width:8px;height:14px;opacity:.9;animation:confettiFall linear forwards}@keyframes confettiFall{to{transform:translateY(120vh) rotate(720deg)}}`;const s2=document.createElement('style');s2.id='confetti-styles';s2.textContent=css2;document.head.appendChild(s2);} 
                      const balloons=()=>{const colors=['#2E8B57','#3CB371','#20B2AA','#66CDAA','#90EE90','#32CD32','#228B22','#7FFFD4'];const cont=document.createElement('div');cont.className='balloons-container';document.body.appendChild(cont);for(let i=0;i<24;i++){const b=document.createElement('div');b.className='balloon';const size=18+Math.random()*18;b.style.width=size+'px';b.style.height=size*1.25+'px';b.style.left=(Math.random()*100)+'%';const dur=5+Math.random()*3;b.style.animationDuration=dur+'s';b.style.animationDelay=(Math.random()*0.8)+'s';b.style.background=colors[Math.floor(Math.random()*colors.length)];cont.appendChild(b);}setTimeout(()=>cont.remove(),8000)};
                      const confetti=()=>{const colors=['#ff6b6b','#ffd93d','#6bcb77','#4d96ff','#9b5de5','#f15bb5','#00bbf9','#2E8B57'];const cont=document.createElement('div');cont.className='confetti-container';document.body.appendChild(cont);for(let i=0;i<120;i++){const c=document.createElement('div');c.className='confetti';const size=6+Math.random()*6;c.style.width=size+'px';c.style.height=(size*1.5)+'px';c.style.left=(Math.random()*100)+'%';c.style.background=colors[Math.floor(Math.random()*colors.length)];c.style.animationDuration=(4+Math.random()*3)+'s';c.style.animationDelay=(Math.random()*0.5)+'s';cont.appendChild(c);}setTimeout(()=>cont.remove(),6000)};
                      try{balloons();confetti();}catch(e){}
                    })();
                </script>
                """,
                unsafe_allow_html=True,
                )
                st.info("Login required")
        
        with col_b:
            if st.button("📋 Copy Link", use_container_width=True):
                st.code("https://priyankatenderfinal-unlhs2yudbpg2ipxgdggws.streamlit.app/")
                st.success("Link copied!")
                st.markdown(
                """
                <script>
                  (function(){
                    if(!document.getElementById('balloon-styles')){const css=`.balloons-container{position:fixed;inset:0;pointer-events:none;overflow:hidden;z-index:9999}.balloon{position:absolute;bottom:-10%;width:22px;height:28px;border-radius:50% 50% 45% 45%;opacity:.9;animation:floatUp linear forwards}.balloon:after{content:'';position:absolute;bottom:-8px;left:50%;transform:translateX(-50%);width:2px;height:10px;background:rgba(0,0,0,.2)}@keyframes floatUp{to{transform:translateY(-120vh)}}`;const s=document.createElement('style');s.id='balloon-styles';s.textContent=css;document.head.appendChild(s);} 
                    if(!document.getElementById('confetti-styles')){const css2=`.confetti-container{position:fixed;inset:0;pointer-events:none;overflow:hidden;z-index:9999}.confetti{position:absolute;top:-10%;width:8px;height:14px;opacity:.9;animation:confettiFall linear forwards}@keyframes confettiFall{to{transform:translateY(120vh) rotate(720deg)}}`;const s2=document.createElement('style');s2.id='confetti-styles';s2.textContent=css2;document.head.appendChild(s2);} 
                    const balloons=()=>{const colors=['#2E8B57','#3CB371','#20B2AA','#66CDAA','#90EE90','#32CD32','#228B22','#7FFFD4'];const cont=document.createElement('div');cont.className='balloons-container';document.body.appendChild(cont);for(let i=0;i<18;i++){const b=document.createElement('div');b.className='balloon';const size=16+Math.random()*16;b.style.width=size+'px';b.style.height=size*1.25+'px';b.style.left=(Math.random()*100)+'%';const dur=5+Math.random()*3;b.style.animationDuration=dur+'s';b.style.animationDelay=(Math.random()*0.8)+'s';b.style.background=colors[Math.floor(Math.random()*colors.length)];cont.appendChild(b);}setTimeout(()=>cont.remove(),7000)};
                    const confetti=()=>{const colors=['#ff6b6b','#ffd93d','#6bcb77','#4d96ff','#9b5de5','#f15bb5','#00bbf9','#2E8B57'];const cont=document.createElement('div');cont.className='confetti-container';document.body.appendChild(cont);for(let i=0;i<90;i++){const c=document.createElement('div');c.className='confetti';const size=6+Math.random()*6;c.style.width=size+'px';c.style.height=(size*1.5)+'px';c.style.left=(Math.random()*100)+'%';c.style.background=colors[Math.floor(Math.random()*colors.length)];c.style.animationDuration=(4+Math.random()*3)+'s';c.style.animationDelay=(Math.random()*0.5)+'s';cont.appendChild(c);}setTimeout(()=>cont.remove(),5000)};
                    try{balloons();confetti();}catch(e){}
                  })();
                </script>
                """,
                unsafe_allow_html=True,
                )
        
        with col_c:
            st.markdown("🔗 [Direct Link](https://priyankatenderfinal-unlhs2yudbpg2ipxgdggws.streamlit.app/)")

# Navigation
create_back_button()

# Run main function
if __name__ == "__main__":
    main()