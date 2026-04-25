#!/usr/bin/env python3
import sys

def main():
    # sys.argv คือ List ที่เก็บ Parameter ทั้งหมดที่ส่งเข้ามา
    # แต่ต้องระวัง! sys.argv[0] จะเป็นชื่อไฟล์โปรแกรมเสมอ 
    # เราจึงต้องหักตัวมันเองออก 1 ตำแหน่ง
    num_params = len(sys.argv) - 1

    # แสดงผลจำนวน Parameter ตามด้วยขึ้นบรรทัดใหม่
    print(f"Number of parameters: {num_params}")

if __name__ == "__main__":
    main()