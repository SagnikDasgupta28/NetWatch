
import time

from database import (
    initialize_database,
    insert_event,
    get_statistics
)

from simulator import generate_event


def main():
    print("=" * 45)
    print("          NETWATCH ENGINE v0.1")
    print("=" * 45)

    initialize_database()

    print("\nDatabase initialized.")
    print("Traffic monitoring simulator started.\n")

    try:
        while True:
            event = generate_event()

            insert_event(event)

            print(
                f"[{event['protocol']}] "
                f"{event['src_ip']} -> {event['dst_ip']} | "
                f"UPLOAD: {event['bytes_sent']} B | "
                f"DOWNLOAD: {event['bytes_received']} B"
            )

            stats = get_statistics()

            print(
                f"TOTAL EVENTS: {stats['total_events']} | "
                f"TOTAL UPLOAD: {stats['uploaded_bytes']} B | "
                f"TOTAL DOWNLOAD: {stats['downloaded_bytes']} B"
            )

            print("-" * 45)

            time.sleep(2)

    except KeyboardInterrupt:
        print("\nNetWatch stopped.")

        stats = get_statistics()
        print("\nFINAL STATISTICS")
        print(stats)


if __name__ == "__main__":
    main()
