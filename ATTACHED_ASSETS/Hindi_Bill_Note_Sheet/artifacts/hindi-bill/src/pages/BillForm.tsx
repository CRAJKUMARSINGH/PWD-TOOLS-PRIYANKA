import { useState } from "react";

type YesNo = "Yes" | "No";
type OrigDep = "Original" | "Deposit";

interface FormData {
  billTitle: string;
  budgetHead: string;
  agreementNo: string;
  mbNo: string;
  subDivision: string;
  nameOfWork: string;
  nameOfContractor: string;
  originalOrDeposit: OrigDep;
  dateOfCommencement: string;
  dateOfCompletion: string;
  actualDateOfCompletion: string;
  totalWorkOrderAmount: string;
  sumPaymentLastBill: string;
  amountThisBill: string;
  uptoDateBillOverride: string;
  dateOfMeasurement: string;
  checkingDateAEN: string;
  selectionItemsCheckedEE: string;
  otherInputs: string;
  isRepairMaintenance: YesNo;
  hasExtraItem: YesNo;
  extraItemAmount: string;
  hasExcessItem: YesNo;
  sd10: string;
  it2: string;
  gst2: string;
  lc1: string;
  depV: string;
  dateOfBillSubmission: string;
  signatoryName: string;
  officeName: string;
}

function formatDate(dateStr: string): string {
  if (!dateStr) return "---";
  const d = new Date(dateStr);
  if (isNaN(d.getTime())) return dateStr;
  return d.toLocaleDateString("en-IN", { day: "2-digit", month: "2-digit", year: "numeric" });
}

function daysBetween(d1: string, d2: string): number {
  if (!d1 || !d2) return 0;
  return Math.round(
    (new Date(d2).getTime() - new Date(d1).getTime()) / (1000 * 60 * 60 * 24)
  );
}

const defaultForm: FormData = {
  billTitle: "RUNNING/FINAL BILL SCRUTINY SHEET",
  budgetHead: "8443-00-108-00-00",
  agreementNo: "",
  mbNo: "",
  subDivision: "",
  nameOfWork: "",
  nameOfContractor: "",
  originalOrDeposit: "Deposit",
  dateOfCommencement: "",
  dateOfCompletion: "",
  actualDateOfCompletion: "",
  totalWorkOrderAmount: "",
  sumPaymentLastBill: "0",
  amountThisBill: "",
  uptoDateBillOverride: "",
  dateOfMeasurement: "",
  checkingDateAEN: "",
  selectionItemsCheckedEE: "",
  otherInputs: "",
  isRepairMaintenance: "No",
  hasExtraItem: "No",
  extraItemAmount: "0",
  hasExcessItem: "No",
  sd10: "",
  it2: "",
  gst2: "",
  lc1: "",
  depV: "0",
  dateOfBillSubmission: "",
  signatoryName: "प्रेमलता जैन, AAO",
  officeName: "PWD Electric Circle, Udaipur",
};

// ── Balloon component ─────────────────────────────────────────────────────────
const BALLOONS = [
  { color: "#ff69b4", left: "5%",  delay: "0s",   dur: "4s"  },
  { color: "#c2185b", left: "15%", delay: "0.6s",  dur: "3.5s" },
  { color: "#ff1493", left: "28%", delay: "1.2s",  dur: "5s"  },
  { color: "#ad1457", left: "42%", delay: "0.3s",  dur: "4.2s" },
  { color: "#f48fb1", left: "57%", delay: "0.9s",  dur: "3.8s" },
  { color: "#e91e63", left: "70%", delay: "1.5s",  dur: "4.6s" },
  { color: "#880e4f", left: "83%", delay: "0.5s",  dur: "3.2s" },
  { color: "#ff80ab", left: "93%", delay: "1.1s",  dur: "4.8s" },
];

function Balloons() {
  return (
    <div style={{ position: "absolute", top: 0, left: 0, width: "100%", height: "100%", overflow: "hidden", pointerEvents: "none" }}>
      {BALLOONS.map((b, i) => (
        <div key={i} style={{
          position: "absolute",
          bottom: "0",
          left: b.left,
          animation: `floatBalloon ${b.dur} ${b.delay} ease-in-out infinite`,
        }}>
          <div style={{
            width: 28,
            height: 34,
            borderRadius: "50% 50% 50% 50% / 60% 60% 40% 40%",
            background: b.color,
            boxShadow: `inset -4px -4px 8px rgba(0,0,0,0.2), inset 4px 4px 8px rgba(255,255,255,0.3)`,
            position: "relative",
          }}>
            <div style={{
              position: "absolute",
              bottom: -2,
              left: "50%",
              transform: "translateX(-50%)",
              width: 3,
              height: 3,
              background: b.color,
              borderRadius: "0 0 50% 50%",
            }} />
          </div>
          <div style={{
            width: 1,
            height: 20,
            background: "rgba(255,255,255,0.5)",
            margin: "0 auto",
          }} />
        </div>
      ))}
    </div>
  );
}

export default function BillForm() {
  const [form, setForm] = useState<FormData>(defaultForm);

  const set = (field: keyof FormData) =>
    (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement>) => {
      let value = e.target.value;
      
      // Auto-prefix contractor name with "M/s." if not already present
      if (field === "nameOfContractor" && value && !value.startsWith("M/s.") && !value.startsWith("m/s.")) {
        value = "M/s. " + value;
      }
      
      setForm(prev => ({ ...prev, [field]: value }));
    };

  // ── Calculations ──────────────────────────────────────────────────────────
  const workOrderAmt = parseFloat(form.totalWorkOrderAmount) || 0;
  const lastBillAmt  = parseFloat(form.sumPaymentLastBill) || 0;
  const thisBillAmt  = parseFloat(form.amountThisBill) || 0;
  const extraAmt     = parseFloat(form.extraItemAmount) || 0;

  const overrideUpto = parseFloat(form.uptoDateBillOverride) || 0;
  const actualExpenditure = overrideUpto > 0 ? overrideUpto : (lastBillAmt + thisBillAmt);

  const rawBalance = workOrderAmt - actualExpenditure;
  const balanceDisplay = rawBalance < 0 ? "Nil" : `Rs. ${rawBalance.toLocaleString("en-IN")}`;

  const sd10 = form.sd10 !== "" ? parseFloat(form.sd10) : Math.round(thisBillAmt * 0.1);
  const it2  = form.it2  !== "" ? parseFloat(form.it2)  : Math.round(thisBillAmt * 0.02);
  const rawGst = thisBillAmt * 0.02;
  const gstCalc = Math.round(rawGst) % 2 === 0 ? Math.round(rawGst) : Math.round(rawGst) + 1;
  const gst2 = form.gst2 !== "" ? parseFloat(form.gst2) : gstCalc;
  const lc1  = form.lc1  !== "" ? parseFloat(form.lc1)  : Math.round(thisBillAmt * 0.01);
  const depV  = parseFloat(form.depV) || 0;

  const totalDeductions = sd10 + it2 + gst2 + lc1 + depV;
  const chequeAmount    = thisBillAmt - totalDeductions;
  const totalCheck      = totalDeductions + chequeAmount;

  const progressPct  = workOrderAmt > 0 ? ((actualExpenditure / workOrderAmt) * 100).toFixed(2) : "0.00";
  const pctNum       = parseFloat(progressPct);
  const extraPct     = workOrderAmt > 0 ? ((extraAmt / workOrderAmt) * 100).toFixed(2) : "0.00";
  const extraExceeds5 = parseFloat(extraPct) > 5;

  const delayDays       = daysBetween(form.dateOfCompletion, form.actualDateOfCompletion);
  const scheduleDuration = daysBetween(form.dateOfCommencement, form.dateOfCompletion);

  // Auto-detect bill submission delay: if date filled → check >= 180 days; if not filled → no note
  const submissionDelayDays = daysBetween(form.actualDateOfCompletion, form.dateOfBillSubmission);
  const lateSubmission = form.dateOfBillSubmission !== "" && submissionDelayDays >= 180;

  // ── Note Generator (VBA-faithful) ─────────────────────────────────────────
  function generateNotePoints(): string[] {
    const pts: string[] = [];
    let n = 1;

    // 1. Work completion %
    pts.push(`${n++}. कार्य ${progressPct} प्रतिशत संपादित हुआ है।`);

    // 2. Deviation — auto based on work %
    // < 90%        → deviation received, this office approval
    // 90–100%      → no deviation note
    // 100–105%     → deviation received, OVERALL EXCESS ≤ 5%, this office
    // > 105%       → deviation received, OVERALL EXCESS > 5%, Superintending Engineer
    if (pctNum < 90) {
      pts.push(`${n++}. जिसका डेविएशन स्टेटमेंट भी स्वीकृति हेतु प्राप्त हुआ है, जिसकी स्वीकृति इसी कार्यालय के क्षेत्राधिकार में निहित है।`);
    } else if (pctNum > 100 && pctNum <= 105) {
      pts.push(`${n++}. जिसका डेविएशन स्टेटमेंट भी स्वीकृति हेतु प्राप्त हुआ है, OVERALL EXCESS वर्क आर्डर राशि के 5% से कम या बराबर है जिसकी स्वीकृति इसी कार्यालय के क्षेत्राधिकार में निहित है।`);
    } else if (pctNum > 105) {
      pts.push(`${n++}. जिसका डेविएशन स्टेटमेंट भी स्वीकृति हेतु प्राप्त हुआ है, OVERALL EXCESS वर्क आर्डर राशि के 5% से अधिक है जिसकी स्वीकृति Superintending Engineer, ${form.officeName} कार्यालय के क्षेत्राधिकार में निहित है।`);
    }

    // 3. Delay / on-time
    if (delayDays > 0) {
      pts.push(`${n++}. कार्य में ${delayDays} दिन की देरी हुई है।`);
      // 4. Time extension authority
      if (scheduleDuration > 0 && delayDays > scheduleDuration / 2) {
        pts.push(`${n++}. टाइम एक्सटेंशन केस Superintending Engineer, ${form.officeName} कार्यालय द्वारा अनुमोदित किया जाना है।`);
      } else {
        pts.push(`${n++}. टाइम एक्सटेंशन केस इस कार्यालय द्वारा अनुमोदित किया जाना है।`);
      }
    } else {
      pts.push(`${n++}. कार्य समय पर संपादित हुआ है।`);
    }

    // 5. Extra item — triggered by flag ONLY (no amount guard)
    if (form.hasExtraItem === "Yes") {
      if (extraExceeds5) {
        pts.push(`${n++}. कार्य सम्पादन में केवल Rs. ${extraAmt.toLocaleString("en-IN")} के अतिरिक्त आइटम सम्पादित किये गये हैं जिसकी राशि वर्क आर्डर राशि की ${extraPct}% होकर 5% से अधिक है जिसकी स्वीकृति Superintending Engineer, ${form.officeName} कार्यालय के क्षेत्राधिकार में है।`);
      } else {
        pts.push(`${n++}. कार्य सम्पादन में केवल Rs. ${extraAmt.toLocaleString("en-IN")} के अतिरिक्त आइटम सम्पादित किये गये हैं जिसकी राशि वर्क आर्डर राशि की ${extraPct}% होकर 5% से कम या बराबर है जिसकी स्वीकृति इस कार्यालय के क्षेत्राधिकार में है।`);
      }
    }

    // 6. Excess quantity — based on work % directly
    if (form.hasExcessItem === "Yes") {
      if (pctNum < 100) {
        pts.push(`${n++}. कार्य संपादन में वर्क आर्डर के जिन आइटम्स में EXCESS QUANTITY संपादित की गई है, उनका विवरण संलग्न है। कार्य में saving है (अर्थात Overall Excess = NIL), जिसकी स्वीकृति इस कार्यालय के क्षेत्राधिकार में है।`);
      } else if (pctNum <= 105) {
        const ep = (pctNum - 100).toFixed(2);
        pts.push(`${n++}. कार्य संपादन में वर्क आर्डर के जिन आइटम्स में EXCESS QUANTITY संपादित की गई है, उनका विवरण संलग्न है। कार्य में OVERALL EXCESS केवल ${ep}% होकर 5% से कम या बराबर है, जिसकी स्वीकृति इस कार्यालय के क्षेत्राधिकार में है।`);
      } else {
        const ep = (pctNum - 100).toFixed(2);
        pts.push(`${n++}. कार्य संपादन में वर्क आर्डर के जिन आइटम्स में EXCESS QUANTITY संपादित की गई है, उनका विवरण संलग्न है। कार्य में OVERALL EXCESS ${ep}% होकर 5% से अधिक है, जिसकी स्वीकृति Superintending Engineer, ${form.officeName} कार्यालय के क्षेत्राधिकार में है।`);
      }
    }

    // 7. QC Report — always
    pts.push(`${n++}. गुणवत्ता नियंत्रण (Q.C.) परीक्षण रिपोर्ट संलग्न हैं।`);

    // 8. Hand Over — when NOT repair/maintenance
    if (form.isRepairMaintenance === "No") {
      pts.push(`${n++}. हस्तांतरण विवरण Hand Over Statement संलग्न है।`);
    }

    // 9. Bill submission delay — AUTO from dates (no manual flag)
    if (lateSubmission) {
      pts.push(`${n++}. कार्य समाप्ति के करीब 6 महीने बाद फाइनल बिल इस कार्यालय में प्रस्तुत किया गया है। इस अप्रत्याशित देरी के लिए सहायक अभियंता से स्पष्टीकरण मांगा जाए ऐसी प्रस्तावना है।`);
    }

    // 10. Conclusion — always
    pts.push(`${n++}. बिल समुचित निर्णय हेतु प्रस्तुत है।`);

    return pts;
  }

  const notePoints = generateNotePoints();

  // ── Output rows ───────────────────────────────────────────────────────────
  const outputRows: [string, string][] = [
    ["1. Budget Head", form.budgetHead || "---"],
    ["2. Agreement No.", form.agreementNo || "---"],
    ["3. MB No. & Page", form.mbNo || "---"],
    ["4. Name of Sub Division", form.subDivision || "---"],
    ["5. Name of Work", form.nameOfWork || "---"],
    ["6. Name of Contractor", form.nameOfContractor || "---"],
    ["7. Original / Deposit", form.originalOrDeposit],
    ["8. Date of Commencement", formatDate(form.dateOfCommencement)],
    ["9. Date of Completion (Scheduled)", formatDate(form.dateOfCompletion)],
    ["10. Actual Date of Completion", formatDate(form.actualDateOfCompletion)],
    ["11. Total Amount of Work Order", `Rs. ${workOrderAmt.toLocaleString("en-IN")}`],
    ["12A. Sum of payment up to last bill", `Rs. ${lastBillAmt.toLocaleString("en-IN")}`],
    ["12B. Amount of this bill", `Rs. ${thisBillAmt.toLocaleString("en-IN")}`],
    ["12C. Actual expenditure up to this bill (A+B)", `Rs. ${actualExpenditure.toLocaleString("en-IN")}`],
    ["13. Balance to be done = (11 − 12C)", balanceDisplay],
    ["14. Prorata Progress on the Work", "Evident from para 10 and 12 above."],
    ["15. Date of record Measurement (JEN/AEN)", formatDate(form.dateOfMeasurement)],
    ["16. Date of Checking & % checked by AEN", form.checkingDateAEN || "---"],
    ["17. No. of selection items checked by EE", form.selectionItemsCheckedEE || ""],
    ["18. Other Inputs", form.otherInputs || ""],
    ["(A) Is it a Repair / Maintenance Work", form.isRepairMaintenance],
    ["(B) Extra Item", form.hasExtraItem],
    ["    Amount of Extra Items", `Rs. ${extraAmt.toLocaleString("en-IN")}`],
    ["(C) Any Excess Item", form.hasExcessItem],
    // Only show bill submission delay if date is entered
    ...(form.dateOfBillSubmission !== "" ? [["(D) Bill Submission Delay (auto)", lateSubmission ? `Yes — ${submissionDelayDays} days` : `No — ${submissionDelayDays} days`] as [string, string]] : []),
    ["Date of Bill Submission", formatDate(form.dateOfBillSubmission)],
  ];

  const deductionRows: [string, string][] = [
    ["SD @ 10%", `Rs. ${sd10.toLocaleString("en-IN")}`],
    ["IT @ 2%", `Rs. ${it2.toLocaleString("en-IN")}`],
    ["GST @ 2%", `Rs. ${gst2.toLocaleString("en-IN")}`],
    ["LC @ 1%", `Rs. ${lc1.toLocaleString("en-IN")}`],
    ["Dep-V", `Rs. ${depV.toLocaleString("en-IN")}`],
    ["Cheque / Amount", `Rs. ${chequeAmount.toLocaleString("en-IN")}`],
    ["Total", `Rs. ${totalCheck.toLocaleString("en-IN")}`],
  ];

  // ── Print ─────────────────────────────────────────────────────────────────
  function handlePrint() {
    const html = buildPrintHtml(form.billTitle, outputRows, deductionRows, notePoints, form.signatoryName);
    const win = window.open("", "_blank", "width=794,height=1123");
    if (!win) { alert("Please allow popups to print."); return; }
    win.document.write(html);
    win.document.close();
    win.focus();
    setTimeout(() => { win.print(); win.close(); }, 500);
  }

  const inputCls   = "w-full border border-pink-300 rounded px-2 py-1 text-sm focus:outline-none focus:ring-1 focus:ring-pink-500 bg-white";
  const labelCls   = "text-xs font-semibold text-pink-900 mb-1 block";
  const sectionCls = "bg-white rounded-xl border border-pink-200 p-4 mb-4 shadow-sm";

  return (
    <>
      <style>{`
        @keyframes floatBalloon {
          0%   { transform: translateY(0px) rotate(-4deg); }
          50%  { transform: translateY(-18px) rotate(4deg); }
          100% { transform: translateY(0px) rotate(-4deg); }
        }
        @keyframes shimmer {
          0%   { background-position: -200% center; }
          100% { background-position: 200% center; }
        }
      `}</style>

      <div className="min-h-screen" style={{ background: "linear-gradient(135deg, #fce4ec 0%, #f8bbd0 50%, #fce4ec 100%)" }}>

        {/* ── Header with Balloons ── */}
        <div style={{
          position: "relative",
          background: "linear-gradient(90deg, #880e4f, #c2185b, #e91e63, #c2185b, #880e4f)",
          backgroundSize: "200% auto",
          animation: "shimmer 4s linear infinite",
          overflow: "hidden",
          padding: "14px 0",
        }}>
          <Balloons />
          <div style={{ position: "relative", zIndex: 1, textAlign: "center", color: "#fff", fontWeight: 700, fontSize: "1.1rem", letterSpacing: "0.05em", textShadow: "0 2px 4px rgba(0,0,0,0.3)" }}>
            🌸 हिंदी बिल नोट शीट जनरेटर &nbsp;|&nbsp; Hindi Bill Note Sheet Generator 🌸
          </div>
        </div>

        <div className="flex flex-col lg:flex-row gap-4 p-4 max-w-[1400px] mx-auto">

          {/* ── INPUT FORM ── */}
          <div className="lg:w-1/2 flex flex-col">
            <div style={{ background: "linear-gradient(135deg, #fce4ec, #f8bbd0)", border: "1px solid #f48fb1" }} className="rounded-xl p-3 mb-4">
              <h2 className="font-bold text-sm" style={{ color: "#880e4f" }}>📝 इनपुट फॉर्म / Input Form — Bill Details</h2>
              <p className="text-xs mt-1" style={{ color: "#c2185b" }}>विवरण भरें, नोट शीट स्वतः अपडेट होगी / Fill details, note sheet updates automatically</p>
            </div>

            {/* Basic Info */}
            <div className={sectionCls}>
              <h3 className="font-bold text-sm mb-3 border-b pb-1" style={{ color: "#880e4f", borderColor: "#f48fb1" }}>मूल जानकारी / Basic Information</h3>
              <div className="grid grid-cols-1 gap-3">
                <div>
                  <label className={labelCls}>बिल शीर्षक / Bill Title</label>
                  <input className={inputCls} value={form.billTitle} onChange={set("billTitle")} />
                </div>
                <div className="grid grid-cols-2 gap-2">
                  <div>
                    <label className={labelCls}>1. बजट शीर्ष / Budget Head</label>
                    <input className={inputCls} value={form.budgetHead} onChange={set("budgetHead")} />
                  </div>
                  <div>
                    <label className={labelCls}>2. अनुबंध संख्या / Agreement No.</label>
                    <input className={inputCls} value={form.agreementNo} onChange={set("agreementNo")} placeholder="e.g. 62/2024-25" />
                  </div>
                </div>
                <div className="grid grid-cols-2 gap-2">
                  <div>
                    <label className={labelCls}>3. एम.बी. संख्या व पृष्ठ / MB No. & Page</label>
                    <input className={inputCls} value={form.mbNo} onChange={set("mbNo")} placeholder="e.g. 813/Page 84-85" />
                  </div>
                  <div>
                    <label className={labelCls}>4. उप-खंड का नाम / Sub Division Name</label>
                    <input className={inputCls} value={form.subDivision} onChange={set("subDivision")} placeholder="e.g. Udaipur" />
                  </div>
                </div>
                <div>
                  <label className={labelCls}>5. कार्य का नाम / Name of Work</label>
                  <textarea className={inputCls} rows={2} value={form.nameOfWork} onChange={set("nameOfWork")} />
                </div>
                <div className="grid grid-cols-2 gap-2">
                  <div>
                    <label className={labelCls}>6. ठेकेदार का नाम / Contractor Name</label>
                    <input className={inputCls} value={form.nameOfContractor} onChange={set("nameOfContractor")} placeholder="M/s. ..." />
                  </div>
                  <div>
                    <label className={labelCls}>7. मूल / जमा / Original / Deposit</label>
                    <select className={inputCls} value={form.originalOrDeposit} onChange={set("originalOrDeposit")}>
                      <option>Original</option>
                      <option>Deposit</option>
                    </select>
                  </div>
                </div>
              </div>
            </div>

            {/* Dates & Amounts */}
            <div className={sectionCls}>
              <h3 className="font-bold text-sm mb-3 border-b pb-1" style={{ color: "#880e4f", borderColor: "#f48fb1" }}>तिथियाँ व राशि / Dates & Amounts</h3>
              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label className={labelCls}>8. प्रारंभ तिथि / Date of Commencement</label>
                  <input type="date" className={inputCls} value={form.dateOfCommencement} onChange={set("dateOfCommencement")} />
                </div>
                <div>
                  <label className={labelCls}>9. पूर्णता तिथि (निर्धारित) / Date of Completion</label>
                  <input type="date" className={inputCls} value={form.dateOfCompletion} onChange={set("dateOfCompletion")} />
                </div>
                <div>
                  <label className={labelCls}>10. वास्तविक पूर्णता तिथि / Actual Completion Date</label>
                  <input type="date" className={inputCls} value={form.actualDateOfCompletion} onChange={set("actualDateOfCompletion")} />
                </div>
                <div>
                  <label className={labelCls}>
                    बिल प्रस्तुति तिथि / Bill Submission Date
                    {lateSubmission && <span className="ml-1 text-red-600 font-bold">⚠️ &gt;180 days</span>}
                  </label>
                  <input type="date" className={inputCls} value={form.dateOfBillSubmission} onChange={set("dateOfBillSubmission")} />
                </div>
                <div>
                  <label className={labelCls}>11. कुल कार्यादेश राशि / Total Work Order Amount (₹)</label>
                  <input type="number" className={inputCls} value={form.totalWorkOrderAmount} onChange={set("totalWorkOrderAmount")} placeholder="0" />
                </div>
                <div>
                  <label className={labelCls}>12A. पिछले बिल तक भुगतान / Payment Upto Last Bill (₹)</label>
                  <input type="number" className={inputCls} value={form.sumPaymentLastBill} onChange={set("sumPaymentLastBill")} placeholder="0" />
                </div>
                <div>
                  <label className={labelCls}>12B. इस बिल की राशि / Amount of This Bill (₹)</label>
                  <input type="number" className={inputCls} value={form.amountThisBill} onChange={set("amountThisBill")} placeholder="0" />
                </div>
                <div>
                  <label className={labelCls}>15. माप तिथि / Date of Measurement (JEN/AEN)</label>
                  <input type="date" className={inputCls} value={form.dateOfMeasurement} onChange={set("dateOfMeasurement")} />
                </div>
              </div>
            </div>

            {/* Conditions */}
            <div className={sectionCls}>
              <h3 className="font-bold text-sm mb-3 border-b pb-1" style={{ color: "#880e4f", borderColor: "#f48fb1" }}>शर्तें / Conditions & Flags</h3>
              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label className={labelCls}>(A) मरम्मत/रखरखाव कार्य? / Repair/Maintenance Work?</label>
                  <select className={inputCls} value={form.isRepairMaintenance} onChange={set("isRepairMaintenance")}>
                    <option>Yes</option><option>No</option>
                  </select>
                </div>
                <div>
                  <label className={labelCls}>(B) अतिरिक्त मद? / Extra Item Executed?</label>
                  <select className={inputCls} value={form.hasExtraItem} onChange={set("hasExtraItem")}>
                    <option>Yes</option><option>No</option>
                  </select>
                </div>
                {form.hasExtraItem === "Yes" && (
                  <div className="col-span-2">
                    <label className={labelCls}>अतिरिक्त मद राशि / Extra Items Amount (₹)</label>
                    <input type="number" className={inputCls} value={form.extraItemAmount} onChange={set("extraItemAmount")} placeholder="0" />
                    <p className={`text-xs mt-1 font-semibold ${extraExceeds5 ? "text-red-600" : "text-green-700"}`}>
                      {extraPct}% —&nbsp;
                      {extraExceeds5 ? "⚠️ >5%: SE approval needed" : "✓ ≤5%: Approved"}
                    </p>
                  </div>
                )}
                <div>
                  <label className={labelCls}>(C) अधिक मात्रा? / Any Excess Quantity?</label>
                  <select className={inputCls} value={form.hasExcessItem} onChange={set("hasExcessItem")}>
                    <option>Yes</option><option>No</option>
                  </select>
                </div>
              </div>
            </div>

            {/* Deductions - Simplified */}
            <div className={sectionCls}>
              <h3 className="font-bold text-sm mb-3 border-b pb-1" style={{ color: "#880e4f", borderColor: "#f48fb1" }}>कटौतियाँ / Deductions</h3>
              <div className="grid grid-cols-1 gap-3">
                <div>
                  <label className={labelCls}>Dep-V (₹) [अन्य कटौतियाँ स्वचालित / Other deductions automated]</label>
                  <input type="number" className={inputCls} value={form.depV} onChange={set("depV")} />
                </div>
              </div>
            </div>

            {/* Other Details */}
            <div className={sectionCls}>
              <h3 className="font-bold text-sm mb-3 border-b pb-1" style={{ color: "#880e4f", borderColor: "#f48fb1" }}>अन्य विवरण / Other Details</h3>
              <div className="grid grid-cols-1 gap-3">
                <div>
                  <label className={labelCls}>16. जाँच तिथि व % (AEN) / Checking Date & % by AEN</label>
                  <input className={inputCls} value={form.checkingDateAEN} onChange={set("checkingDateAEN")} placeholder="e.g. 01/03/2025, 100%" />
                </div>
                <div>
                  <label className={labelCls}>17. EE द्वारा जाँची गई मदें / Selection Items Checked by EE</label>
                  <input className={inputCls} value={form.selectionItemsCheckedEE} onChange={set("selectionItemsCheckedEE")} placeholder="(optional)" />
                </div>
                <div>
                  <label className={labelCls}>18. अन्य इनपुट / Other Inputs</label>
                  <input className={inputCls} value={form.otherInputs} onChange={set("otherInputs")} placeholder="(optional)" />
                </div>
                <div className="grid grid-cols-2 gap-2">
                  <div>
                    <label className={labelCls}>हस्ताक्षरकर्ता नाम / Signatory Name</label>
                    <input className={inputCls} value={form.signatoryName} onChange={set("signatoryName")} />
                  </div>
                  <div>
                    <label className={labelCls}>कार्यालय नाम / Office Name</label>
                    <input className={inputCls} value={form.officeName} onChange={set("officeName")} placeholder="PWD Electric Circle, Udaipur" />
                  </div>
                </div>
              </div>
            </div>

            <button
              onClick={handlePrint}
              className="w-full font-bold py-3 rounded-xl text-sm transition-all mb-6 shadow-lg"
              style={{
                background: "linear-gradient(90deg, #880e4f, #e91e63, #880e4f)",
                backgroundSize: "200% auto",
                color: "#fff",
                animation: "shimmer 3s linear infinite",
                border: "none",
                cursor: "pointer",
              }}
            >
              🖨️ Print Note Sheet (A4 — no header/footer)
            </button>
          </div>

          {/* ── LIVE PREVIEW ── */}
          <div className="lg:w-1/2">
            <div className="rounded-xl p-3 mb-4" style={{ background: "linear-gradient(135deg, #fce4ec, #f8bbd0)", border: "1px solid #f48fb1" }}>
              <h2 className="font-bold text-sm" style={{ color: "#880e4f" }}>👁 Live Preview — Note Sheet Output</h2>
              <p className="text-xs mt-1" style={{ color: "#c2185b" }}>Exactly what will print on A4 with 10 mm margins.</p>
            </div>
            <NoteSheetTable
              billTitle={form.billTitle}
              outputRows={outputRows}
              deductionRows={deductionRows}
              notePoints={notePoints}
              signatoryName={form.signatoryName}
            />
          </div>
        </div>
      </div>
    </>
  );
}

// ── Shared table renderer ─────────────────────────────────────────────────────

interface TableProps {
  billTitle: string;
  outputRows: [string, string][];
  deductionRows: [string, string][];
  notePoints: string[];
  signatoryName: string;
}

function NoteSheetTable({ billTitle, outputRows, deductionRows, notePoints, signatoryName }: TableProps) {
  const tdL = "border border-gray-500 px-2 py-1 font-semibold bg-gray-50 w-1/2 align-top text-xs";
  const tdR = "border border-gray-500 px-2 py-1 w-1/2 align-top text-xs";

  return (
    <div className="bg-white border border-gray-400 text-black text-xs overflow-auto" style={{ fontFamily: "'Noto Sans Devanagari','Segoe UI',sans-serif" }}>
      <table className="w-full border-collapse">
        <thead>
          <tr>
            <td colSpan={2} className="border border-gray-500 text-center font-bold py-2 text-sm" style={{ background: "#fce4ec", color: "#880e4f" }}>
              {billTitle || "BILL SCRUTINY SHEET"}
            </td>
          </tr>
        </thead>
        <tbody>
          {outputRows.map(([label, value], i) => (
            <tr key={i}>
              <td className={tdL}>{label}</td>
              <td className={tdR}>{value}</td>
            </tr>
          ))}
          <tr>
            <td colSpan={2} className="border border-gray-500 px-2 py-1 font-bold bg-gray-100 text-xs">
              Deductions:- &nbsp; Rs.
            </td>
          </tr>
          {deductionRows.map(([label, value], i) => (
            <tr key={i}>
              <td className={tdL + " pl-6"}>{label}</td>
              <td className={tdR}>{value}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <div className="border-t border-gray-500 p-3">
        <ol className="list-none space-y-1 text-xs leading-relaxed">
          {notePoints.map((pt, i) => <li key={i}>{pt}</li>)}
        </ol>
        <div className="mt-4 text-center text-xs font-semibold">
          {signatoryName}
        </div>
      </div>
    </div>
  );
}

// ── Print HTML ────────────────────────────────────────────────────────────────

function buildPrintHtml(
  billTitle: string,
  outputRows: [string, string][],
  deductionRows: [string, string][],
  notePoints: string[],
  signatoryName: string,
): string {
  const rowsHtml = outputRows
    .map(([l, v]) => `<tr><td class="l">${l}</td><td class="r">${v}</td></tr>`)
    .join("");
  const dedHtml = deductionRows
    .map(([l, v]) => `<tr><td class="l" style="padding-left:1.5em">${l}</td><td class="r">${v}</td></tr>`)
    .join("");
  const notesHtml = notePoints.map(pt => `<li>${pt}</li>`).join("");

  return `<!DOCTYPE html>
<html lang="hi">
<head>
<meta charset="UTF-8"/>
<title>${billTitle}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari:wght@400;600;700&display=swap" rel="stylesheet">
<style>
  @page { 
    size: A4 portrait; 
    margin: 10mm;
  }
  * { box-sizing:border-box; margin:0; padding:0; }
  body { font-family:'Noto Sans Devanagari','Segoe UI',sans-serif; font-size:9pt; color:#000; background:#fff; }
  table { width:100%; border-collapse:collapse; }
  td { border:1px solid #555; padding:2px 5px; vertical-align:top; }
  .h  { text-align:center; font-weight:700; font-size:10pt; background:#fce4ec; color:#880e4f; padding:4px; }
  .l  { font-weight:600; background:#f5f5f5; width:50%; }
  .r  { width:50%; }
  .dh { font-weight:700; background:#ebebeb; }
  .note-section { border:1px solid #555; border-top:none; padding:8px; }
  ol { list-style:none; padding:0; }
  li { margin-bottom:3px; line-height:1.6; }
  .sig { text-align:center; font-weight:600; margin-top:16px; }
</style>
</head>
<body>
<table>
  <tr><td colspan="2" class="h">${billTitle}</td></tr>
  ${rowsHtml}
  <tr><td colspan="2" class="dh">Deductions:- &nbsp; Rs.</td></tr>
  ${dedHtml}
</table>
<div class="note-section">
  <ol>${notesHtml}</ol>
  <div class="sig">${signatoryName}</div>
</div>
</body>
</html>`;
}
