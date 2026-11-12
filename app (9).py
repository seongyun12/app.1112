"""재산 한눈에 | GitHub + Streamlit Community Cloud
같은 폴더에 requirements.txt를 두고 streamlit run app.py 실행.
GitHub에 두 파일을 올리고 Streamlit Community Cloud에서 app.py 배포.
배포된 공개 주소의 QR코드를 만들면 스마트폰으로 접속할 수 있습니다.
금액 입력은 브라우저 안에서만 계산합니다. 별도 저장·계좌 연동 없음.
"""
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="재산 한눈에", page_icon="🌿", layout="centered")
st.markdown("""<style>
[data-testid="stHeader"],[data-testid="stToolbar"],footer{display:none!important}
[data-testid="stAppViewContainer"]{background:#f2f4f6}
.block-container,[data-testid="stMainBlockContainer"]{padding:0!important;max-width:500px!important}
[data-testid="stVerticalBlock"]{gap:0!important}
iframe{display:block;width:100%;height:100svh!important;border:0}
</style>""", unsafe_allow_html=True)
PAGE = r'''<!doctype html><html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<style>
*{box-sizing:border-box}html,body{margin:0;background:#f2f4f6;color:#191f28;font-family:system-ui,-apple-system,'Apple SD Gothic Neo','Malgun Gothic',sans-serif}body{padding:16px}main{max-width:460px;margin:auto}h1{font-size:25px;letter-spacing:-1px;margin:0 0 5px}.intro{font-size:15px;color:#596574;margin:0 0 14px;line-height:1.45}.card{background:white;padding:17px;border-radius:20px;margin-bottom:10px}h2{font-size:18px;margin:0 0 12px;letter-spacing:-.5px}.unit{font-size:13px;color:#596574;font-weight:400;float:right;margin-top:3px}.grid{display:grid;grid-template-columns:1fr 1fr;gap:12px 14px}label{font-size:15px;font-weight:600;display:block}.hint{font-size:12px;font-weight:400;color:#596574;display:block;margin-top:2px}.field{display:flex;align-items:center;border-bottom:1px solid #c5cdd7;margin-top:3px;gap:4px}.field:focus-within{border-color:#2266e8;box-shadow:0 1px #2266e8}input{min-width:0;width:100%;height:42px;background:none;border:0;outline:0;color:#191f28;font:600 20px system-ui;text-align:right}input::placeholder{color:#9aa4b1;font-size:16px;font-weight:400}.field span{font-size:13px;color:#596574;white-space:nowrap}.line{display:flex;justify-content:space-between;gap:10px;align-items:center;font-size:15px}.line strong{font-size:22px;letter-spacing:-.5px;overflow-wrap:anywhere;text-align:right}.sub{font-size:14px;color:#596574;line-height:1.5;margin:8px 0 0}.blue{color:#2266e8}.purchase{display:flex;align-items:center;gap:14px}.purchase label{flex:1}.purchase .field{width:48%;margin:0}.answer{font-size:20px;line-height:1.35;letter-spacing:-.5px;margin:13px 0 0;font-weight:750}.fine{font-size:12px;line-height:1.5;color:#596574;margin:8px 3px}.warn{color:#ad4615}.safe{color:#2266e8}
@media(max-height:760px){body{padding:10px 13px}.intro{margin-bottom:10px}.card{padding:13px 15px;margin-bottom:8px}h2{margin-bottom:9px}.grid{gap:8px 13px}input{height:37px}.answer{margin-top:9px;font-size:19px}.sub{margin-top:6px}.fine{font-size:11px;margin-top:6px}h1{font-size:23px}}
</style></head><body><main>
<h1>재산 한눈에</h1><p class="intro">금액만 적어 주세요. 아래에서 바로 알려드려요.</p>
<section class="card" aria-labelledby="entry"><h2 id="entry">내 돈 적기 <span class="unit">단위: 만원</span></h2>
<div class="grid">
<label for="cash">통장에 있는 돈<span class="hint">지금 꺼내 쓸 수 있는 돈</span><div class="field"><input id="cash" type="text" inputmode="decimal" maxlength="12" placeholder="예: 500" autocomplete="off"><span>만원</span></div></label>
<label for="invest">주식·펀드<span class="hint">지금 팔았을 때의 금액</span><div class="field"><input id="invest" type="text" inputmode="decimal" maxlength="12" placeholder="없으면 0" autocomplete="off"><span>만원</span></div></label>
<label for="locked">집·보증금<span class="hint">내 집값 또는 돌려받을 보증금</span><div class="field"><input id="locked" type="text" inputmode="decimal" maxlength="12" placeholder="없으면 0" autocomplete="off"><span>만원</span></div></label>
<label for="debt">갚을 돈<span class="hint">남은 대출 등 빚의 합계</span><div class="field"><input id="debt" type="text" inputmode="decimal" maxlength="12" placeholder="없으면 0" autocomplete="off"><span>만원</span></div></label>
</div></section>
<section class="card" aria-live="polite" aria-atomic="true"><div class="line"><span>빚을 뺀 내 재산</span><strong id="net">—</strong></div><p class="sub" id="liquid">위에 금액을 적으면 바로 계산돼요.</p></section>
<section class="card" aria-labelledby="buy"><h2 id="buy">이거 사도 괜찮을까?</h2>
<div class="grid"><label for="monthly">한 달 꼭 쓰는 돈<span class="hint">생활비 + 대출 갚는 돈</span><div class="field"><input id="monthly" type="text" inputmode="decimal" maxlength="12" placeholder="예: 150" autocomplete="off"><span>만원</span></div></label>
<label for="price">사고 싶은 물건값<span class="hint">통장에서 한 번에 낼 금액</span><div class="field"><input id="price" type="text" inputmode="decimal" maxlength="12" placeholder="예: 100" autocomplete="off"><span>만원</span></div></label></div>
<div role="status" aria-live="polite" aria-atomic="true"><p class="answer" id="answer">두 금액을 적어 주세요</p><p class="sub" id="detail">사고 난 뒤에도 생활비 3개월치가 남는지 봐드려요.</p></div>
</section>
<p class="fine">빈칸은 0으로 계산해요. 집값은 대출을 빼기 전 금액으로, 같은 돈은 한 번만 적어 주세요. 입력 내용은 저장하지 않아요.</p>
<p class="fine">생활비 3개월치는 비교 기준일 뿐 안전을 보장하지 않아요. 수입·세금·자산 매각·대출 일시상환은 반영하지 않아요.</p>
</main><script>
'use strict';
const ids=['cash','invest','locked','debt','monthly','price'];
const el=id=>document.getElementById(id);
const money=n=>n.toLocaleString('ko-KR',{maximumFractionDigits:2})+'만원';
const round=n=>Math.round(n*100)/100;
function analyze(c,i,l,d,m,p){const total=round(c+i+l);const after=round(c-p);const target=round(m*3);return {total,net:round(total-d),ratio:total>0?c/total*100:null,after,target,shortage:round(Math.max(0,target-after)),limit:round(Math.max(0,c-target)),state:after<0?'short':m<=0?'missing':after<target?'reserve':'ok'};}
let timer;
function update(){
 const vals=ids.map(id=>Number(el(id).value)||0);const [c,i,l,d,m,p]=vals;
 const a=analyze(...vals);const any=ids.slice(0,4).some(id=>el(id).value!=='');
 el('net').textContent=any?money(a.net):'—';
 el('liquid').textContent=a.total>0?'그중 바로 쓸 수 있는 돈은 '+money(c)+' ('+a.ratio.toLocaleString('ko-KR',{maximumFractionDigits:1})+'%)예요.':any?'현재 바로 쓸 수 있는 돈은 0원이에요.':'위에 금액을 적으면 바로 계산돼요.';
 if(a.net<0)el('liquid').textContent+=' 가진 재산보다 갚을 돈이 많아요.';
 const answer=el('answer'),detail=el('detail');answer.className='answer';
 if(el('cash').value===''){answer.textContent='통장에 있는 돈부터 적어 주세요';detail.textContent='지금 꺼내 쓸 수 있는 돈을 기준으로 계산해요.';return;}
 if(el('monthly').value===''||el('price').value===''){answer.textContent='생활비와 물건값을 적어 주세요';detail.textContent='사고 난 뒤에도 생활비 3개월치가 남는지 봐드려요.';return;}
 if(a.state==='short'){answer.textContent='통장에 '+money(-a.after)+'이 부족해요';answer.classList.add('warn');detail.textContent='주식이나 집을 팔지 않고, 지금 통장에 있는 돈만 비교했어요.';return;}
 if(a.state==='missing'){answer.textContent='구매 후 '+money(a.after)+'이 남아요';detail.textContent='한 달 꼭 쓰는 돈을 0보다 크게 적어야 생활비 여유를 확인할 수 있어요.';return;}
 if(a.state==='reserve'){answer.textContent='사면 생활비 여유가 줄어요';answer.classList.add('warn');detail.textContent='구매 후 '+money(a.after)+'. 생활비 3개월치('+money(a.target)+')보다 '+money(a.shortage)+' 적어요.';}
 else{answer.textContent='사도 생활비 3개월치는 남아요';answer.classList.add('safe');detail.textContent='구매 후 통장에 '+money(a.after)+'이 남아요. 생활비 3개월치는 '+money(a.target)+'이에요.';}
}
ids.forEach(id=>el(id).addEventListener('input',()=>{let v=el(id).value.replace(/[^0-9.]/g,'');const parts=v.split('.');v=parts[0].slice(0,8)+(parts.length>1?'.'+parts.slice(1).join('').slice(0,2):'');if(v!==el(id).value)el(id).value=v;clearTimeout(timer);timer=setTimeout(update,220);}));
update();
</script></body></html>'''
components.html(PAGE, height=850, scrolling=True)
