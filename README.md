# EC2 Metadata CLI Tool

A lightweight Python CLI tool to fetch AWS EC2 instance metadata using IMDSv2 (Instance Metadata Service Version 2).  
Supports full metadata dumps as well as individual field queries via flag-style arguments.

---

## 🔧 Features

- ✅ Fetch full instance metadata in JSON format
- ✅ Query specific metadata fields via command-line flags (e.g. `--instance-id`, `--ami-id`)
- ✅ Uses secure IMDSv2 token-based requests
- ✅ Outputs valid JSON in all cases
- ✅ Minimal dependencies (just `requests`)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.6+
- Must be run **from within an EC2 instance**
- Install the required Python dependency:

```bash
pip install requests
```

---

## 🧪 Usage

### Run the script

#### ✅ Fetch all metadata:

```bash
python ec2_metadata.py
```

#### ✅ Fetch specific metadata fields:

```bash
python ec2_metadata.py --instance-id --ami-id
```

---

## 🧾 Example Output

### 🔹 All metadata:

```json
{
  "instance-id": "i-0123456789abcdef0",
  "instance-type": "t3.micro",
  "ami-id": "ami-0abcdef1234567890",
  "hostname": "ip-172-31-0-1.ec2.internal",
  "local-ipv4": "172.31.0.1",
  "public-ipv4": "34.229.11.88",
  "availability-zone": "us-east-1a",
  "security-groups": "default"
}
```

### 🔹 Specific fields:

```bash
python ec2_metadata.py --ami-id --instance-id
```

```json
{
  "ami-id": "ami-0abcdef1234567890",
  "instance-id": "i-0123456789abcdef0"
}
```

---

## 🏷️ Supported Flags

| Flag                  | Metadata Field              |
|-----------------------|-----------------------------|
| `--instance-id`       | EC2 Instance ID             |
| `--instance-type`     | Instance Type (e.g. `t3.micro`) |
| `--ami-id`            | Amazon Machine Image ID     |
| `--hostname`          | EC2 Internal Hostname       |
| `--local-ipv4`        | Private IPv4 Address        |
| `--public-ipv4`       | Public IPv4 Address (if any)|
| `--availability-zone` | Availability Zone           |
| `--security-groups`   | Assigned Security Groups    |

---

## 🔐 Security Notes

- This tool uses **IMDSv2** for all metadata queries.
- Do **not** expose this script or EC2 metadata APIs to public or untrusted users.
- Public IP will only be returned if the instance has one and is in a public subnet.

---

## 📁 File Structure

```
.
├── ec2_metadata.py   # Main CLI script
├── README.md         # You're here!
```

---

## 📜 License

This project is licensed under the MIT License. You are free to use, modify, and distribute it with attribution.

---

## 🙋‍♀️ Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Submit a pull request with a clear explanation

---

## ✉️ Contact

For issues, feedback, or feature requests, please open a GitHub Issue.

