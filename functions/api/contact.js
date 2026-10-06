/**
 * Cloudflare Pages Function: /api/contact
 * Handles contact form submissions and delivers lead emails via SendGrid v3 Mail Send API.
 */

export async function onRequestOptions() {
  return new Response(null, {
    status: 204,
    headers: {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "POST, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type",
      "Access-Control-Max-Age": "86400"
    }
  });
}

export async function onRequestPost(context) {
  const { request, env } = context;

  const corsHeaders = {
    "Access-Control-Allow-Origin": "*",
    "Content-Type": "application/json"
  };

  try {
    let name = "";
    let email = "";
    let company = "";
    let interest = "General inquiry";
    let message = "";
    let honeypot = "";

    const contentType = request.headers.get("content-type") || "";

    if (contentType.includes("application/json")) {
      const data = await request.json();
      name = (data.name || "").trim();
      email = (data.email || "").trim();
      company = (data.company || "").trim();
      interest = (data.interest || "General inquiry").trim();
      message = (data.message || "").trim();
      honeypot = (data._gotcha || data.website || "").trim();
    } else {
      // Form-encoded or FormData
      const formData = await request.formData();
      name = (formData.get("name") || "").toString().trim();
      email = (formData.get("email") || "").toString().trim();
      company = (formData.get("company") || "").toString().trim();
      interest = (formData.get("interest") || "General inquiry").toString().trim();
      message = (formData.get("message") || "").toString().trim();
      honeypot = (formData.get("_gotcha") || formData.get("website") || "").toString().trim();
    }

    // 1. Silent Bot Trap (Honeypot)
    if (honeypot) {
      console.warn("[Bot Alert] Honeypot triggered, silently dropping submission.");
      return new Response(JSON.stringify({ ok: true, id: "bot_filtered" }), {
        status: 200,
        headers: corsHeaders
      });
    }

    // 2. Field Validation
    if (!name || !email || !company || !message) {
      return new Response(
        JSON.stringify({
          ok: false,
          error: "Missing required fields: name, work email, company, and message are required."
        }),
        { status: 400, headers: corsHeaders }
      );
    }

    if (!email.includes("@") || !email.includes(".")) {
      return new Response(
        JSON.stringify({ ok: false, error: "Please enter a valid work email address." }),
        { status: 400, headers: corsHeaders }
      );
    }

    // 3. Check for SendGrid API Key
    const sendgridApiKey = env.SENDGRID_API_KEY;
    if (!sendgridApiKey) {
      console.error("SENDGRID_API_KEY is not defined in Cloudflare Pages environment variables.");
      return new Response(
        JSON.stringify({
          ok: false,
          error: "SendGrid is not configured yet. Please configure SENDGRID_API_KEY in Cloudflare Pages environment variables.",
          fallback_email: "sales@ntrust.ai"
        }),
        { status: 503, headers: corsHeaders }
      );
    }

    // 4. Construct Email Payload
    const receiverRaw = env.CONTACT_RECEIVER_EMAIL || "naveed@ntrust.ai,sales@ntrust.ai";
    const toRecipients = receiverRaw
      .split(",")
      .map((addr) => addr.trim())
      .filter((addr) => addr.length > 0)
      .map((addr) => ({ email: addr }));

    const fromEmail = env.SENDGRID_FROM_EMAIL || "noreply@ntrust.ai";
    const fromName = env.SENDGRID_FROM_NAME || "nTrust.ai Website Contact";

    const clientIp = request.headers.get("cf-connecting-ip") || "Unknown";
    const clientCountry = request.headers.get("cf-ipcountry") || "Unknown";
    const timestamp = new Date().toUTCString();

    const emailSubject = `[nTrust Inquiry] ${interest} from ${name} (${company})`;

    const emailHtml = `
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1e293b; }
    .card { max-width: 600px; margin: 20px auto; border: 1px solid #e2e8f0; border-radius: 8px; overflow: hidden; }
    .header { background: #0f172a; color: #ffffff; padding: 20px; text-align: left; }
    .header h2 { margin: 0; font-size: 20px; color: #38bdf8; }
    .header p { margin: 4px 0 0 0; color: #94a3b8; font-size: 13px; }
    .content { padding: 24px; background: #ffffff; }
    .field-table { width: 100%; border-collapse: collapse; margin-bottom: 20px; }
    .field-table td { padding: 8px 12px; border-bottom: 1px solid #f1f5f9; font-size: 14px; }
    .field-table td.label { font-weight: 600; color: #475569; width: 140px; background: #f8fafc; }
    .message-box { background: #f8fafc; border-left: 4px solid #38bdf8; padding: 16px; border-radius: 4px; font-size: 14px; white-space: pre-wrap; word-break: break-word; }
    .footer { background: #f1f5f9; padding: 12px 20px; font-size: 12px; color: #64748b; text-align: center; }
  </style>
</head>
<body>
  <div class="card">
    <div class="header">
      <h2>🛡️ nTrust.ai &mdash; New Lead Captured</h2>
      <p>Submitted via ntrust.ai/contact on ${timestamp}</p>
    </div>
    <div class="content">
      <table class="field-table">
        <tr><td class="label">Full Name</td><td><strong>${escapeHtml(name)}</strong></td></tr>
        <tr><td class="label">Work Email</td><td><a href="mailto:${escapeHtml(email)}">${escapeHtml(email)}</a></td></tr>
        <tr><td class="label">Company</td><td>${escapeHtml(company)}</td></tr>
        <tr><td class="label">Interest Area</td><td><strong>${escapeHtml(interest)}</strong></td></tr>
        <tr><td class="label">Visitor IP / Geo</td><td>${escapeHtml(clientIp)} (${escapeHtml(clientCountry)})</td></tr>
      </table>

      <h4 style="margin: 20px 0 8px 0; color: #0f172a;">Message:</h4>
      <div class="message-box">${escapeHtml(message)}</div>
    </div>
    <div class="footer">
      This is an automated notification dispatched by nTrust Cloudflare Pages Edge Functions via SendGrid.
    </div>
  </div>
</body>
</html>
`;

    const emailText = `
New Lead from nTrust.ai Contact Form:
------------------------------------
Name: ${name}
Work Email: ${email}
Company: ${company}
Interest: ${interest}
Time: ${timestamp}
Location: ${clientIp} (${clientCountry})

Message:
${message}
`;

    const sendgridPayload = {
      personalizations: [
        {
          to: toRecipients,
          subject: emailSubject
        }
      ],
      from: {
        email: fromEmail,
        name: fromName
      },
      reply_to: {
        email: email,
        name: name
      },
      content: [
        {
          type: "text/plain",
          value: emailText.trim()
        },
        {
          type: "text/html",
          value: emailHtml.trim()
        }
      ]
    };

    // 5. Send Email via SendGrid REST API
    const sgResponse = await fetch("https://api.sendgrid.com/v3/mail/send", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${sendgridApiKey}`,
        "Content-Type": "application/json"
      },
      body: JSON.stringify(sendgridPayload)
    });

    if (sgResponse.status === 202 || sgResponse.status === 200) {
      return new Response(
        JSON.stringify({
          ok: true,
          message: "Thank you! Your message has been sent successfully."
        }),
        { status: 200, headers: corsHeaders }
      );
    } else {
      const errText = await sgResponse.text();
      console.error(`SendGrid API error (${sgResponse.status}):`, errText);
      return new Response(
        JSON.stringify({
          ok: false,
          error: "Failed to deliver email through SendGrid. Please email sales@ntrust.ai directly.",
          status: sgResponse.status
        }),
        { status: 502, headers: corsHeaders }
      );
    }
  } catch (err) {
    console.error("Unhandled error in /api/contact:", err);
    return new Response(
      JSON.stringify({
        ok: false,
        error: "An internal server error occurred while processing your request."
      }),
      { status: 500, headers: corsHeaders }
    );
  }
}

function escapeHtml(str) {
  if (!str) return "";
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}
